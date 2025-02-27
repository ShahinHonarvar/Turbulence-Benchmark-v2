from collections import Counter

def palindromes_between_indices(s):
    s = s.lower()
    sub = ''.join([c for c in s[4:8] if c.isalpha()])
    if len(sub) < 5:
        return set()

    def can_form_palindrome(freq):
        odd_count = sum((1 for count in freq.values() if count % 2 != 0))
        return odd_count <= 1

    def generate_palindromes(chars, half, mid, length, left, right, palindromes):
        if left > right:
            if len(half + mid) == length:
                palindromes.add(half + mid + half[::-1])
            return
        for i, c in enumerate(chars):
            new_half = half + c
            new_chars = chars[:i] + chars[i + 1:]
            generate_palindromes(new_chars, new_half, mid, length, left + 1, right, palindromes)
    freq = Counter(sub)
    if not can_form_palindrome(freq):
        return set()
    chars = []
    mid = ''
    for c, count in freq.items():
        chars.extend([c] * (count // 2))
        if count % 2 != 0:
            mid = c
    palindromes_set = set()
    generate_palindromes(chars, '', mid, 5, 0, len(chars) - 1, palindromes_set)
    return palindromes_set
from collections import Counter

def palindromes_between_indices(s):
    if len(s) < 5:
        return set()
    substring = s[3:5].lower()
    char_count = Counter(filter(str.isalpha, substring))

    def can_form_palindrome(counts):
        odd_count = sum((1 for count in counts.values() if count % 2 != 0))
        return odd_count <= 1
    if not can_form_palindrome(char_count):
        return set()

    def generate_palindromes(half, middle):
        if len(half) == 0:
            return {middle}
        palindromes = set()
        for i in range(len(half)):
            if i > 0 and half[i] == half[i - 1]:
                continue
            new_half = half[:i] + half[i + 1:]
            palindromes.update(generate_palindromes(new_half, half[i] + middle + half[i]))
        return palindromes
    half = ''.join((char * (count // 2) for char, count in char_count.items()))
    middle = ''.join((char for char, count in char_count.items() if count % 2 != 0))
    return {p for p in generate_palindromes(half, middle) if len(p) >= 3}
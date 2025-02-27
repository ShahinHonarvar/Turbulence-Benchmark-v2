from collections import Counter

def palindromes_between_indices(s):
    if len(s) < 10:
        return set()
    substring = s[8:10].lower()

    def can_form_palindrome(counter):
        odd_count = sum((1 for count in counter.values() if count % 2 != 0))
        return odd_count <= 1

    def generate_palindromes(counter, half, odd_char, length):
        if len(half) == length // 2:
            full_palindrome = half + odd_char + half[::-1]
            return {full_palindrome}
        palindromes = set()
        for char in counter:
            if counter[char] > 0:
                counter[char] -= 2
                palindromes.update(generate_palindromes(counter, half + char, odd_char, length))
                counter[char] += 2
        return palindromes
    counter = Counter(filter(str.isalpha, substring))
    if not can_form_palindrome(counter):
        return set()
    odd_char = ''
    for char in counter:
        if counter[char] % 2 != 0:
            odd_char = char
            counter[char] -= 1
            break
    palindromes = set()
    for length in range(3, len(substring) + 1):
        palindromes.update(generate_palindromes(counter.copy(), '', odd_char, length))
    return palindromes
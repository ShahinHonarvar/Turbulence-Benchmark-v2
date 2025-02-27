from functools import reduce

def palindromes_between_indices(s):

    def is_palindrome(s):
        return s == s[::-1]

    def get_substring_english_letters(s):
        return ''.join((c for c in s if c.isalpha())).lower()

    def generate_permutations(s, max_length=6):
        if max_length == 1:
            return s
        permutations = set()
        for i in range(len(s) - max_length + 1):
            for j in range(i, len(s)):
                if j - i + 1 >= max_length:
                    permutations.add(s[i:j + 1])
        return permutations

    def filter_palindromes(permutations):
        return [p for p in permutations if is_palindrome(p)]
    substring = get_substring_english_letters(s[:6])
    permutations = generate_permutations(substring)
    palindromes = filter_palindromes(permutations)
    return set(palindromes)
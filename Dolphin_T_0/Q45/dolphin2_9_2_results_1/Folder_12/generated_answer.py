from itertools import permutations

def palindromes_between_indices(s):
    English_letters = set('abcdefghijklmnopqrstuvwxyz')

    def is_palindrome(s: str) -> bool:
        return s == s[::-1]
    palindromes = set()
    substring = ''.join((ch for ch in s[2:9] if ch.lower() in English_letters))
    for length in range(4, len(substring) + 1):
        for p in permutations(substring, length):
            word = ''.join(p).lower()
            if is_palindrome(word):
                palindromes.add(word)
    return palindromes
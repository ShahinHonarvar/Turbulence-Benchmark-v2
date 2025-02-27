from itertools import permutations

def is_palindrome(s):
    return s == s[::-1]

def palindromes_between_indices(s):
    if len(s) < 8:
        return set()
    substring = s[3:8].lower()
    filtered_chars = [ch for ch in substring if ch.isalpha()]
    if len(filtered_chars) < 4:
        return set()
    palindromes = set()
    for length in range(4, len(filtered_chars) + 1):
        for perm in permutations(filtered_chars, length):
            word = ''.join(perm)
            if is_palindrome(word):
                palindromes.add(word)
    return palindromes
from itertools import permutations

def is_palindrome(s):
    return s == s[::-1]

def palindromes_between_indices(s):
    s = s[1:8].lower()
    english_letters = ''.join(filter(str.isalpha, s))
    palindromes = set()
    for perm in permutations(english_letters):
        candidate = ''.join(perm)
        if len(candidate) >= 7 and is_palindrome(candidate):
            palindromes.add(candidate)
    return palindromes
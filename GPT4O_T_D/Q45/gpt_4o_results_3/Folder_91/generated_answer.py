from itertools import permutations

def is_palindrome(s):
    return s == s[::-1]

def palindromes_between_indices(s):
    english_letters = [char.lower() for char in s[2:7] if char.isalpha()]
    resulting_palindromes = set()
    if len(english_letters) >= 3:
        for perm in permutations(english_letters, 3):
            candidate = ''.join(perm)
            if is_palindrome(candidate):
                resulting_palindromes.add(candidate)
    return resulting_palindromes
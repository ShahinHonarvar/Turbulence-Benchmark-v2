from itertools import permutations

def is_palindrome(s):
    return s == s[::-1]

def palindromes_between_indices(s):
    if len(s) < 4:
        return set()
    substr = s[0:4].lower()
    alphabetic_chars = [c for c in substr if c.isalpha()]
    if len(alphabetic_chars) < 4:
        return set()
    potential_palindromes = set()
    for length in range(4, len(alphabetic_chars) + 1):
        for perm in permutations(alphabetic_chars, length):
            potential_word = ''.join(perm)
            if is_palindrome(potential_word):
                potential_palindromes.add(potential_word)
    return potential_palindromes
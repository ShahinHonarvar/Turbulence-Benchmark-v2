from itertools import permutations

def is_palindrome(s):
    return s == s[::-1]

def palindromes_between_indices(s):
    s = s[:4].lower()
    english_letters = ''.join(filter(str.isalpha, s))
    all_permutations = set((''.join(p) for i in range(3, len(english_letters) + 1) for p in permutations(english_letters, i)))
    palindromes_set = {word for word in all_permutations if is_palindrome(word)}
    return palindromes_set
from collections import Counter
from itertools import permutations

def is_palindrome(s):
    return s == s[::-1]

def palindromes_between_indices(s):
    s = s[1:10].lower()
    letters_only = ''.join(filter(str.isalpha, s))
    letter_counts = Counter(letters_only)
    potential_letters = []
    for letter, count in letter_counts.items():
        potential_letters.extend([letter] * count)
    possible_palindromes = set()
    for i in range(7, len(potential_letters) + 1):
        for perm in set(permutations(potential_letters, i)):
            candidate = ''.join(perm)
            if is_palindrome(candidate):
                possible_palindromes.add(candidate)
    return possible_palindromes
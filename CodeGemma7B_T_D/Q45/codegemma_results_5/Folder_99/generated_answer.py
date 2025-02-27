from itertools import permutations
import re

def palindromes_between_indices(string):
    pattern = '[^a-zA-Z]'
    letters = re.sub(pattern, '', string)
    letters = letters.lower()
    if len(letters) < 5:
        return set()
    palindromes = set()
    for indices in range(4, 9):
        for permutation in permutations(letters[:indices]):
            palindrome = ''.join(permutation)
            palindromes.add(palindrome)
    return palindromes
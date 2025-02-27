from itertools import permutations
import string

def palindromes_between_indices(s):
    substr = s[1:4].lower()
    letters = [char for char in substr if char in string.ascii_lowercase]
    palindromes = set()
    for r in range(4, len(letters) + 1):
        for perm in permutations(letters, r):
            word = ''.join(perm)
            if word == word[::-1]:
                palindromes.add(word)
    return palindromes
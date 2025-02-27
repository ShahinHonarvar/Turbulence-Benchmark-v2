from itertools import permutations
import string

def palindromes_between_indices(s):
    letters = [ch for ch in s[1:6] if ch in string.ascii_lowercase]
    result = set()
    for p in permutations(letters, len(letters)):
        word = ''.join(p)
        if word == word[::-1] and len(word) >= 6:
            result.add(word.lower())
    return result
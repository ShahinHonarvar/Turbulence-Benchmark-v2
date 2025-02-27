import string
import itertools

def palindromes_between_indices(s):
    letters = [c for c in s[4:10] if c.lower() in string.ascii_lowercase]
    palindromes = set()
    for length in range(6, len(letters) + 1):
        for perm in itertools.permutations(letters, length):
            word = ''.join(perm)
            if word.lower() == word.lower()[::-1]:
                palindromes.add(word)
    return palindromes
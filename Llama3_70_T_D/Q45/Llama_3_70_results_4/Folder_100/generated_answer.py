import itertools
import string

def palindromes_between_indices(s):
    s = s[:6].lower()
    letters = [char for char in s if char in string.ascii_lowercase]
    palindromes = set()
    for r in range(6, len(letters) + 1):
        for combo in itertools.combinations(letters, r):
            for perm in itertools.permutations(combo):
                word = ''.join(perm)
                if word == word[::-1]:
                    palindromes.add(word)
    return palindromes
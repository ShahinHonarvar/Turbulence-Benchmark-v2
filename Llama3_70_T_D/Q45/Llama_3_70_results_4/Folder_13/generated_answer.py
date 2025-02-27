import itertools
import re

def palindromes_between_indices(s):
    letters = re.findall('[a-zA-Z]', s[3:10])
    letters = [letter.lower() for letter in letters]
    palindromes = set()
    for r in range(5, len(letters) + 1):
        for combo in itertools.combinations(letters, r):
            for perm in itertools.permutations(combo):
                word = ''.join(perm)
                if word == word[::-1]:
                    palindromes.add(word)
    return palindromes
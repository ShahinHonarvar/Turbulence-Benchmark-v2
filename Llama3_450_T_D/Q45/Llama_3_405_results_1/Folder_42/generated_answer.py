import itertools
import re

def palindromes_between_indices(s):
    s = s[6:10]
    s = re.sub('[^a-zA-Z]', '', s).lower()
    unique_letters = set(s)
    palindromes = set()
    for r in range(3, len(s) + 1):
        for combo in itertools.combinations(s, r):
            for perm in itertools.permutations(combo):
                perm = ''.join(perm)
                if perm == perm[::-1]:
                    palindromes.add(perm)
    return palindromes
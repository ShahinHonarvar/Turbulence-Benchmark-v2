from itertools import permutations

def palindromes_between_indices(s):
    letters = [c for c in s[2:5] if c.isalpha()]
    letters = [c.lower() for c in letters]
    palindromes = set()
    for length in range(4, len(letters) + 1):
        for perm in set(permutations(letters, length)):
            for p in [perm, perm[::-1]]:
                candidate = ''.join(p)
                if len(set(candidate)) == len(candidate) and candidate == candidate[::-1]:
                    palindromes.add(candidate)
    return palindromes
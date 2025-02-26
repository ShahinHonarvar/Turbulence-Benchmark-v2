from itertools import permutations

def palindromes_between_indices(s):
    letters = [c.lower() for c in s[1:6] if c.isalpha()]
    palindromes = set()
    for r in range(5, len(letters) + 1):
        for perm in set(permutations(letters, r)):
            for arrangement in set(permutations(perm)):
                test = ''.join(arrangement)
                if test == test[::-1]:
                    palindromes.add(test)
    return {p for p in palindromes if len(p) >= 5}
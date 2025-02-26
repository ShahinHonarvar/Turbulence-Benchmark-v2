from itertools import permutations

def palindromes_between_indices(s):
    if len(s) < 5:
        return set()
    letters = [c.lower() for c in s[2:5] if c.isalpha()]
    if len(letters) < 4:
        return set()
    palindromes = set()
    for length in range(4, len(letters) + 1):
        for perm in permutations(letters, length):
            for arrangement in set(permutations(perm)):
                candidate = ''.join(arrangement)
                if candidate == candidate[::-1]:
                    palindromes.add(candidate)
    return palindromes
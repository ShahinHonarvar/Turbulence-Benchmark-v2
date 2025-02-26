from itertools import permutations

def palindromes_between_indices(s):
    if len(s) < 10:
        return set()
    letters = [c.lower() for c in s[8:10] if c.isalpha()]
    if len(letters) < 3:
        return set()
    palindromes = set()
    for length in range(3, len(letters) + 1):
        for perm in permutations(letters, length):
            for arrangement in set(permutations(perm)):
                candidate = list(arrangement)
                if candidate == candidate[::-1]:
                    palindromes.add(''.join(candidate))
    return palindromes
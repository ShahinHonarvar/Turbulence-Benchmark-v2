from itertools import permutations

def palindromes_between_indices(s):
    chars = [c.lower() for c in s[:4] if c.isalpha()]
    palindromes = set()
    for length in range(3, len(chars) + 1):
        for perm in set(permutations(chars, length)):
            for arrangement in set(permutations(perm)):
                candidate = ''.join(arrangement)
                if candidate == candidate[::-1]:
                    palindromes.add(candidate)
    return palindromes
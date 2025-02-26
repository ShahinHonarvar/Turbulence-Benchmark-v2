from itertools import permutations

def palindromes_between_indices(s):
    letters = [char.lower() for char in s[2:10] if char.isalpha()]
    if len(letters) < 6:
        return set()
    palindromes = set()
    for perm in set(permutations(letters, 6)):
        for length in range(6, len(perm) + 1):
            for start in range(len(perm) - length + 1):
                candidate = perm[start:start + length]
                if candidate == candidate[::-1]:
                    palindromes.add(''.join(candidate))
    return palindromes
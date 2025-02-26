from itertools import permutations

def palindromes_between_indices(s):
    letters = [char.lower() for char in s[:7] if char.isalpha()]
    palindromes = set()
    for perm in set(permutations(letters, len(letters))):
        for length in range(4, len(perm) + 1):
            for start in range(len(perm) - length + 1):
                subset = perm[start:start + length]
                if len(subset) >= 4:
                    forward = ''.join(subset)
                    backward = forward[::-1]
                    if forward == backward:
                        palindromes.add(forward)
    return palindromes
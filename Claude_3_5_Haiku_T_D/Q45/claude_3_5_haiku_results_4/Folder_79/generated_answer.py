from itertools import permutations

def palindromes_between_indices(s):
    letters = [c.lower() for c in s[1:8] if c.isalpha()]
    palindromes = set()
    for length in range(3, len(letters) + 1):
        for perm in set(permutations(letters, length)):
            for i in range(len(perm) - length + 1):
                subset = perm[i:i + length]
                if list(subset) == list(subset)[::-1]:
                    palindromes.add(''.join(subset))
    return palindromes
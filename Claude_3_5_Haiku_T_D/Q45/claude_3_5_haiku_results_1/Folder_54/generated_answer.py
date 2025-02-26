from itertools import permutations

def palindromes_between_indices(s):
    letters = [c.lower() for c in s[4:10] if c.isalpha()]
    n = len(letters)
    if n < 4:
        return set()
    palindromes = set()
    for length in range(4, n + 1):
        for perm in set(permutations(letters, length)):
            for i in range(len(perm) - length + 1):
                subset = list(perm[i:i + length])
                if subset == subset[::-1]:
                    palindromes.add(''.join(subset))
    return palindromes
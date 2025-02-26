from itertools import permutations

def palindromes_between_indices(s):
    letters = [c.lower() for c in s[2:10] if c.isalpha()]
    palindromes = set()
    for length in range(6, len(letters) + 1):
        for perm in permutations(letters, length):
            for i in range(len(perm) - length + 1):
                subset = perm[i:i + length]
                if len(subset) >= 6:
                    candidate = ''.join(subset)
                    if candidate == candidate[::-1]:
                        palindromes.add(candidate)
    return palindromes
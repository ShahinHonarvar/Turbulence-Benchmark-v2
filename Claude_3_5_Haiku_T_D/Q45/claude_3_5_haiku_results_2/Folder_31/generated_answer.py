from itertools import permutations

def palindromes_between_indices(s):
    letters = [char.lower() for char in s[1:9] if char.isalpha()]
    palindromes = set()
    for r in range(6, len(letters) + 1):
        for perm in set(permutations(letters, r)):
            for i in range(len(perm) - r + 1):
                candidate = perm[i:i + r]
                if len(candidate) >= 6 and ''.join(candidate) == ''.join(candidate)[::-1]:
                    palindromes.add(''.join(candidate))
    return palindromes
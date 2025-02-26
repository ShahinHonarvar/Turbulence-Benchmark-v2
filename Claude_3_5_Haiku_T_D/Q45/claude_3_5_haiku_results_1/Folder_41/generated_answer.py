from itertools import permutations

def palindromes_between_indices(s):
    letters = [char.lower() for char in s[2:4] if char.isalpha()]
    if len(letters) < 3:
        return set()
    palindromes = set()
    for perm in set(permutations(letters)):
        for i in range(len(perm)):
            candidate = list(perm)
            candidate = candidate[i:] + candidate[:i]
            if candidate == candidate[::-1] and len(candidate) >= 3:
                palindromes.add(''.join(candidate))
    return palindromes
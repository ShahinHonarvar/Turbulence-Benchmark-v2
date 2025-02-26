from itertools import permutations

def palindromes_between_indices(s):
    letters = [char.lower() for char in s[4:10] if char.isalpha()]
    if len(letters) < 5:
        return set()
    palindromes = set()
    for perm in set(permutations(letters)):
        for length in range(5, len(perm) + 1):
            for start in range(len(perm) - length + 1):
                curr = perm[start:start + length]
                if list(curr) == list(curr)[::-1]:
                    palindromes.add(''.join(curr))
    return palindromes
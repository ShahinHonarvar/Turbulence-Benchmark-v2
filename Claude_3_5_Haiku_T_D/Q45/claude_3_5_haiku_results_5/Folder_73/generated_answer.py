from itertools import permutations

def palindromes_between_indices(s):
    letters = [char.lower() for char in s[3:7] if char.isalpha()]
    if len(letters) < 3:
        return set()
    palindrome_set = set()
    for perm in set(permutations(letters)):
        for start in range(len(perm) - 2):
            for length in range(3, len(perm) + 1):
                candidate = perm[start:start + length]
                if list(candidate) == list(candidate)[::-1]:
                    palindrome_set.add(''.join(candidate))
    return palindrome_set
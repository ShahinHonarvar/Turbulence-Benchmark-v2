from itertools import permutations

def palindromes_between_indices(s):
    if len(s) < 4:
        return set()
    letters = [char.lower() for char in s[1:4] if char.isalpha()]
    if len(letters) < 4:
        return set()
    palindrome_set = set()
    for perm in set(permutations(letters)):
        for length in range(4, len(perm) + 1):
            for start in range(len(perm) - length + 1):
                candidate = perm[start:start + length]
                if list(candidate) == list(candidate)[::-1]:
                    palindrome_set.add(''.join(candidate))
    return palindrome_set
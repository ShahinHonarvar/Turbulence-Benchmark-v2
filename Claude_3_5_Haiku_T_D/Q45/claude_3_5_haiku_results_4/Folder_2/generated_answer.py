from itertools import permutations

def palindromes_between_indices(s):
    letters = [c.lower() for c in s[1:6] if c.isalpha()]
    palindrome_set = set()
    if len(letters) < 6:
        return palindrome_set
    for perm in set(permutations(letters)):
        for length in range(6, len(letters) + 1):
            for start in range(len(perm) - length + 1):
                candidate = perm[start:start + length]
                if candidate == candidate[::-1]:
                    palindrome_set.add(''.join(candidate))
    return palindrome_set
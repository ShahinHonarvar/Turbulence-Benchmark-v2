from itertools import permutations

def palindromes_between_indices(s):
    letters = [c.lower() for c in s[7:9] if c.isalpha()]
    if len(letters) < 3:
        return set()
    palindrome_set = set()
    for perm in set(permutations(letters)):
        for length in range(3, len(perm) + 1):
            for start in range(len(perm) - length + 1):
                candidate = list(perm[start:start + length])
                if candidate == candidate[::-1]:
                    palindrome_set.add(''.join(candidate))
    return palindrome_set
from itertools import permutations

def palindromes_between_indices(s):
    letters = [c.lower() for c in s[5:10] if c.isalpha()]
    if len(letters) < 4:
        return set()
    palindrome_set = set()
    for perm in set(permutations(letters)):
        for i in range(len(perm) - 3):
            for j in range(i + 4, len(perm) + 1):
                candidate = perm[i:j]
                if len(candidate) >= 4 and list(candidate) == list(candidate)[::-1]:
                    palindrome_set.add(''.join(candidate))
    return palindrome_set
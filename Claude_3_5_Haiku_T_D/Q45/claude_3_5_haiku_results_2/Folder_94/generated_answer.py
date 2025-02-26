from itertools import permutations

def palindromes_between_indices(s):
    if len(s) < 5:
        return set()
    letters = [c.lower() for c in s[3:5] if c.isalpha()]
    if len(letters) < 3:
        return set()
    palindrome_set = set()
    for perm in set(permutations(letters)):
        for length in range(3, len(perm) + 1):
            for start in range(len(perm) - length + 1):
                candidate = perm[start:start + length]
                if list(candidate) == list(candidate)[::-1]:
                    palindrome = ''.join(candidate)
                    palindrome_set.add(palindrome)
    return palindrome_set
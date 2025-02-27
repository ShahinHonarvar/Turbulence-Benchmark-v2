from itertools import permutations

def palindromes_between_indices(s):
    s = s[:6].lower()
    chars = [c for c in s if c.isalpha()]
    palindrome_set = set()
    for length in range(4, len(chars) + 1):
        for perm in set(permutations(chars, length)):
            if perm == perm[::-1]:
                palindrome_set.add(''.join(perm))
    return palindrome_set
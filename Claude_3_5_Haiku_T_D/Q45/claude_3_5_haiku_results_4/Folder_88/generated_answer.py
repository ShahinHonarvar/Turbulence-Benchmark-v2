from itertools import permutations

def palindromes_between_indices(s):
    letters = [c.lower() for c in s[3:8] if c.isalpha()]
    palindrome_set = set()
    for length in range(6, len(letters) + 1):
        for perm in set(permutations(letters, length)):
            candidate = ''.join(perm)
            if len(set(candidate)) >= 3 and candidate == candidate[::-1]:
                palindrome_set.add(candidate)
    return palindrome_set
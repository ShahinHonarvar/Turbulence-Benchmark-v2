from itertools import permutations

def palindromes_between_indices(s):
    letters = [c.lower() for c in s[4:10] if c.isalpha()]
    palindrome_set = set()
    for length in range(4, len(letters) + 1):
        for perm in set(permutations(letters, length)):
            candidate = ''.join(perm)
            if len(candidate) >= 4 and candidate == candidate[::-1]:
                palindrome_set.add(candidate)
    return palindrome_set
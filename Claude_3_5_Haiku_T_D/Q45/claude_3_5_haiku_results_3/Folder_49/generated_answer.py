from itertools import permutations

def palindromes_between_indices(s):
    letters = [c.lower() for c in s[5:8] if c.isalpha()]
    if len(letters) < 3:
        return set()
    palindrome_set = set()
    for perm in set(permutations(letters)):
        for i in range(len(perm)):
            candidate = list(perm)
            left = candidate[:i + 1]
            right = list(reversed(left))
            candidate = left + right[1:]
            if len(candidate) >= 3:
                palindrome = ''.join(candidate)
                palindrome_set.add(palindrome)
    return palindrome_set
from itertools import permutations

def palindromes_between_indices(s):
    letters = [c.lower() for c in s[2:10] if c.isalpha()]
    if len(letters) < 7:
        return set()
    palindrome_set = set()
    for perm in set(permutations(letters, 7)):
        candidate = ''.join(perm)
        if candidate == candidate[::-1]:
            palindrome_set.add(candidate)
    return palindrome_set
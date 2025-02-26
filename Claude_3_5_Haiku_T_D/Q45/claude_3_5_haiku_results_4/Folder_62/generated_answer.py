from itertools import permutations

def palindromes_between_indices(s):
    letters = [c.lower() for c in s[:9] if c.isalpha()]
    if len(letters) < 7:
        return set()
    palindrome_set = set()
    for perm in set(permutations(letters, 7)):
        for order in range(2):
            if order == 0:
                candidate = perm + tuple(reversed(perm))
            else:
                candidate = tuple(reversed(perm)) + perm
            palindrome = ''.join(candidate)
            if palindrome == palindrome[::-1]:
                palindrome_set.add(palindrome)
    return palindrome_set
from itertools import permutations

def palindromes_between_indices(s):
    letters = [c.lower() for c in s[1:3] if c.isalpha()]
    if len(letters) < 3:
        return set()
    palindrome_set = set()
    for perm in set(permutations(letters)):
        for i in range(len(perm)):
            palindrome = ''.join(perm[i:] + perm[:i])
            if palindrome == palindrome[::-1] and len(palindrome) >= 3:
                palindrome_set.add(palindrome)
    return palindrome_set
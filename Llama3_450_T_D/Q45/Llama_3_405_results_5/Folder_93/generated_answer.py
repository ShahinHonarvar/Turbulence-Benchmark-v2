import itertools

def palindromes_between_indices(s):
    letters = [c.lower() for c in s[2:8] if c.isalpha()]
    if len(letters) < 6:
        return set()
    palindromes = set()
    for r in range(6, len(letters) + 1):
        for perm in itertools.permutations(letters, r):
            palindrome = ''.join(perm)
            if palindrome == palindrome[::-1]:
                palindromes.add(palindrome)
    return palindromes
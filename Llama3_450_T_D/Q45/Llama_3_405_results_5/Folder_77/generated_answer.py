import itertools

def palindromes_between_indices(s):
    letters = [c.lower() for c in s[4:7] if c.isalpha()]
    palindromes = set()
    for r in range(4, len(letters) + 1):
        for perm in itertools.permutations(letters, r):
            palindrome = ''.join(perm)
            if palindrome == palindrome[::-1]:
                palindromes.add(palindrome)
    return palindromes
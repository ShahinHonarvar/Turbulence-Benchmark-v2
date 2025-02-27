import itertools

def palindromes_between_indices(s):
    letters = [c for c in s[:4] if c.isalpha()]
    letters = ''.join(letters).lower()
    palindromes = set()
    for r in range(4, len(letters) + 1):
        for perm in itertools.permutations(letters, r):
            palindrome = ''.join(perm)
            if palindrome == palindrome[::-1]:
                palindromes.add(palindrome)
    return palindromes
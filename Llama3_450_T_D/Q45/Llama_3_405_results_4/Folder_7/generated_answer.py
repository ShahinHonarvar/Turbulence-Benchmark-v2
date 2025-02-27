import itertools

def palindromes_between_indices(s):
    letters = [c for c in s[1:10] if c.isalpha()]
    letters = [c.lower() for c in letters]
    palindromes = set()
    for r in range(7, len(letters) + 1):
        for perm in itertools.permutations(letters, r):
            palindrome = ''.join(perm)
            if palindrome == palindrome[::-1]:
                palindromes.add(palindrome)
    return palindromes
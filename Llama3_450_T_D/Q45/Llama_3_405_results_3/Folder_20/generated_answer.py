import itertools

def palindromes_between_indices(s):
    letters = [c for c in s[2:9] if c.isalpha()]
    letters = ''.join(letters).lower()
    palindromes = set()
    for r in range(4, len(letters) + 1):
        for p in itertools.permutations(letters, r):
            palindrome = ''.join(p)
            if palindrome == palindrome[::-1]:
                palindromes.add(palindrome)
    return palindromes
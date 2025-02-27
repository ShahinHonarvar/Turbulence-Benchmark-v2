import itertools

def palindromes_between_indices(s):
    letters = [c for c in s[6:10] if c.isalpha()]
    letters = ''.join(letters).lower()
    if len(letters) < 5:
        return set()
    palindromes = set()
    for r in range(5, len(letters) + 1):
        for c in itertools.combinations(letters, r):
            palindrome = ''.join(c)
            if palindrome == palindrome[::-1]:
                palindromes.add(palindrome)
    return palindromes
import itertools

def palindromes_between_indices(s):
    s = s[2:6]
    letters = set((c.lower() for c in s if c.isalpha()))
    palindromes = set()
    for r in range(3, len(letters) + 1):
        for p in itertools.permutations(letters, r):
            palindrome = ''.join(p)
            if palindrome == palindrome[::-1]:
                palindromes.add(palindrome)
    return palindromes
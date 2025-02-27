import itertools

def palindromes_between_indices(s):
    substring = s[1:8].lower()
    letters = sorted(set((c for c in substring if c.isalpha())))
    palindromes = set()
    for r in range(7, len(letters) + 1):
        for combo in itertools.permutations(letters, r):
            palindrome = ''.join(combo)
            if palindrome == palindrome[::-1]:
                palindromes.add(palindrome)
    return palindromes
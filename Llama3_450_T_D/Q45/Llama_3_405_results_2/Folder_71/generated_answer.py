import itertools

def palindromes_between_indices(s):
    letters = [c for c in s[1:4] if c.isalpha()]
    letters = [c.lower() for c in letters]
    letters = list(set(letters))
    palindromes = set()
    for r in range(2, len(letters) + 1):
        for perm in itertools.permutations(letters, r):
            palindrome = ''.join(perm) + ''.join(perm[::-1])
            if len(palindrome) >= 4:
                palindromes.add(palindrome)
    return palindromes
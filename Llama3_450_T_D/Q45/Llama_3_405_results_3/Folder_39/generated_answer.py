from itertools import permutations

def palindromes_between_indices(s):
    letters = [c for c in s[2:6] if c.isalpha()]
    letters = [c.lower() for c in letters]
    letters = list(set(letters))
    palindromes = set()
    for r in range(3, len(letters) + 1):
        for perm in permutations(letters, r):
            if perm == perm[::-1]:
                palindrome = ''.join(perm)
                palindromes.add(palindrome)
    return palindromes
from itertools import permutations

def palindromes_between_indices(s):
    letters = [c for c in s[1:4] if c.isalpha()]
    if len(letters) < 4:
        return set()
    palindromes = set()
    for r in range(4, len(letters) + 1):
        for p in permutations(letters, r):
            palindrome = ''.join(p).lower()
            if palindrome == palindrome[::-1]:
                palindromes.add(palindrome)
    return palindromes
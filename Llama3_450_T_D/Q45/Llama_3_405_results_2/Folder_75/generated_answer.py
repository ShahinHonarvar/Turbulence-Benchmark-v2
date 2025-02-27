from itertools import permutations

def palindromes_between_indices(s):
    substring = s[2:5].lower()
    letters = [c for c in substring if c.isalpha()]
    palindromes = set()
    for r in range(3, len(letters) + 1):
        for p in permutations(letters, r):
            palindrome = ''.join(p)
            if palindrome == palindrome[::-1]:
                palindromes.add(palindrome)
    return palindromes
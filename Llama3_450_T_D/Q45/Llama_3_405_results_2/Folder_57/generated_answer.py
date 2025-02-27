from itertools import permutations

def palindromes_between_indices(s):
    s = s[2:6].lower()
    letters = [c for c in s if c.isalpha()]
    palindromes = set()
    for r in range(5, len(letters) + 1):
        for p in permutations(letters, r):
            palindrome = ''.join(p)
            if palindrome == palindrome[::-1]:
                palindromes.add(palindrome)
    return palindromes
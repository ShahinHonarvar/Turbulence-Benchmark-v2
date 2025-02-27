from itertools import permutations

def palindromes_between_indices(s):
    chars = [c for c in s[3:8] if c.isalpha()]
    letters = [c.lower() for c in chars]
    palindromes = set()
    for r in range(5, len(letters) + 1):
        for p in permutations(letters, r):
            palindrome = ''.join(p)
            if palindrome == palindrome[::-1]:
                palindromes.add(palindrome)
    return palindromes
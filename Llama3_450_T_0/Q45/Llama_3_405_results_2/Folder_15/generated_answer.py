from itertools import permutations

def palindromes_between_indices(s):
    letters = [c.lower() for c in s[1:3] if c.isalpha()]
    palindromes = set()
    for r in range(3, len(letters) + 1):
        for p in permutations(letters, r):
            palindrome = ''.join(p)
            if palindrome == palindrome[::-1]:
                palindromes.add(palindrome)
    return palindromes
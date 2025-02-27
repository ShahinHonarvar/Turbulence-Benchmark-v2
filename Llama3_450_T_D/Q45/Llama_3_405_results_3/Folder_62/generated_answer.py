from itertools import permutations

def palindromes_between_indices(s):
    letters = [c for c in s[:9].lower() if c.isalpha()]
    palindromes = set()
    for r in range(7, len(letters) + 1):
        for p in permutations(letters, r):
            palindrome = ''.join(p)
            if palindrome == palindrome[::-1]:
                palindromes.add(palindrome)
    return palindromes
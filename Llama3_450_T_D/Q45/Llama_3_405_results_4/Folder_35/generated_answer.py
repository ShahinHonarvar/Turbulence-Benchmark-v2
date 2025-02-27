from itertools import permutations

def palindromes_between_indices(s):

    def is_palindrome(p):
        return p == p[::-1]
    letters = set((c.lower() for c in s[2:5] if c.isalpha()))
    palindromes = set()
    for r in range(4, len(letters) + 1):
        for p in permutations(letters, r):
            palindrome = ''.join(p)
            if is_palindrome(palindrome):
                palindromes.add(palindrome)
    return palindromes
from itertools import permutations

def palindromes_between_indices(s):

    def is_palindrome(t):
        return t == t[::-1]
    letters = [c for c in s[1:3] if c.isalpha()]
    letters = [c.lower() for c in letters]
    palindromes = set()
    for r in range(3, len(letters) + 1):
        for t in permutations(letters, r):
            palindrome = ''.join(t)
            if is_palindrome(palindrome):
                palindromes.add(palindrome)
    return palindromes
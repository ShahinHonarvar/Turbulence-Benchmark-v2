from itertools import permutations

def palindromes_between_indices(s):

    def is_palindrome(p):
        return p == p[::-1]
    letters = [c.lower() for c in s[7:9] if c.isalpha()]
    palindromes = set()
    for r in range(3, len(letters) + 1):
        for p in permutations(letters, r):
            palindrome = ''.join(p)
            if is_palindrome(palindrome):
                palindromes.add(palindrome)
    return palindromes
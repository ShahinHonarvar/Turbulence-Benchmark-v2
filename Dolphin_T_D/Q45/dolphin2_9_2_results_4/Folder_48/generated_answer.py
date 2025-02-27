from itertools import permutations

def palindromes_between_indices(s):

    def is_palindrome(s):
        return s == s[::-1]
    letters = [l for l in s[6:9] if l.isalpha()]
    palindromes = set()
    for r in range(4, len(letters) + 1):
        for p in permutations(letters, r):
            word = ''.join(p).lower()
            if is_palindrome(word):
                palindromes.add(word)
    return palindromes
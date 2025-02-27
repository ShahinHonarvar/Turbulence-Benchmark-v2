from collections import defaultdict

def palindromes_between_indices(s):

    def is_palindrome(s):
        return s == s[::-1]
    letters = defaultdict(int)
    for c in s[2:9]:
        if c.isalpha():
            letters[c.lower()] += 1
    palindromes = set()
    for k, v in letters.items():
        if v >= 4:
            palindromes.add(k * v)
    return palindromes
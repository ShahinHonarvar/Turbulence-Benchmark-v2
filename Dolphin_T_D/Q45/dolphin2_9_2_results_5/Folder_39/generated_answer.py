from itertools import permutations

def palindromes_between_indices(s):

    def convert(s):
        return [c.lower() for c in s]

    def is_palindrome(s):
        return s == s[::-1]
    subset = s[2:6]
    letters = [c.lower() for c in subset]
    palindromes = set()
    for p in permutations(letters, 3):
        if is_palindrome(p):
            palindromes.add(convert(''.join(p)))
    return palindromes
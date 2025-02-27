from itertools import permutations

def palindromes_between_indices(s):

    def is_palindrome(word):
        return word == word[::-1]
    substring = ''.join([c for c in s[4:6] if c.isalpha()]).lower()
    palindromes = {''.join(p) for i in range(3, len(substring) + 1) for p in permutations(substring, i) if is_palindrome(''.join(p))}
    return palindromes
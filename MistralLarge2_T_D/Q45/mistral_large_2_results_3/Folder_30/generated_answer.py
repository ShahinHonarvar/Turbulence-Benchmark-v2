import itertools

def palindromes_between_indices(s):

    def is_palindrome(word):
        return word == word[::-1]
    substring = ''.join([c for c in s[:5] if c.isalpha()]).lower()
    permutations = set(itertools.permutations(substring))
    palindromes = {''.join(p) for p in permutations if is_palindrome(''.join(p)) and len(p) >= 4}
    return palindromes
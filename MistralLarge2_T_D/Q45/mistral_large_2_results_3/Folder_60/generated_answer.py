import itertools

def palindromes_between_indices(s):

    def is_palindrome(word):
        return word == word[::-1]
    substring = ''.join(filter(str.isalpha, s[3:7])).lower()
    permutations = set((''.join(p) for p in itertools.permutations(substring, len(substring))))
    palindromes = {p for p in permutations if is_palindrome(p) and len(p) >= 4}
    return palindromes
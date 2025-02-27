import itertools

def palindromes_between_indices(s):

    def all_permutations(string):
        return [''.join(p) for i in range(len(string)) for p in itertools.permutations(string, i + 1)]

    def is_palindrome(string):
        string = string.lower()
        return string == string[::-1] and len(string) >= 4
    return {p for p in all_permutations(s[1:4]) if is_palindrome(p)}
import itertools

def palindromes_between_indices(s):
    if len(s) < 7:
        return set()

    def is_palindrome(s):
        return s == s[::-1]

    def form_palindrome(s):
        return ''.join(s)

    def get_permutations(s):
        return set(map(form_palindrome, filter(is_palindrome, map(''.join, itertools.product(*[s] * len(s))))))
    s = [c for c in s if c.isalpha()][:7]
    return get_permutations(s)
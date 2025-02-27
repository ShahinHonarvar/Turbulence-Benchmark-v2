from itertools import product

def palindromes_between_indices(str):

    def is_palindrome(s):
        return s.lower() == s.lower()[::-1]
    substrings = [''.join(i) for i in product(*[str[i:j + 1] for i, j in zip(range(7), repeat(7))])]
    return set(filter(lambda x: len(x) >= 4 and is_palindrome(x), substrings))
import itertools

def palindromes_between_indices(s):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'

    def is_palindrome(word):
        return word == word[::-1]
    sub = sorted([c.lower() for c in s[1:6] if c.isalpha()])
    palindromes = set((''.join(word) for length in range(4, 6) for word in itertools.product(sub, repeat=length) if word != tuple(reversed(word)) and is_palindrome(''.join(word))))
    return palindromes
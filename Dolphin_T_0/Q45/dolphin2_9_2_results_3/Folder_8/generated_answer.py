import string
import itertools

def palindromes_between_indices(s):
    letters = [c.lower() for c in s[1:6] if c in string.ascii_letters]
    n = len(letters)
    return set((''.join(i) for i in itertools.product(*[letters] * n) if i == i[::-1] and len(i) >= 5))
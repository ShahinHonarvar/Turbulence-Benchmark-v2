import itertools

def palindromes_between_indices(s):
    letters = ''.join(sorted(set(''.join(s[2:6]))))
    n = len(letter)
    return set(filter(lambda x: len(x) >= 5, [''.join(x) for x in itertools.product(letters, repeat=n)]))
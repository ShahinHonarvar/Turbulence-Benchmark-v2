import itertools
    from string import ascii_letters

def palindromes_between_indices(s):
    s = s[5:10].lower()
    return {i for i in itertools.product(ascii_letters, repeat=5) if i == i[::-1] and ''.join(i).isalpha()}
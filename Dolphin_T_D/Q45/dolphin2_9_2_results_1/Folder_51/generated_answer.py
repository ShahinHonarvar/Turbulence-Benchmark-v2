import itertools

def palindromes_between_indices(s):
    indices = [i for i in range(len(s)) if 3 <= i <= 5]
    english_letters = [c.lower() for c in s if c.isalpha()]
    palindromes = {''.join(p) for p in itertools.product(english_letters, repeat=len(indices)) if ''.join(p) != ''.join(p)[::-1]}
    return palindromes
from itertools import permutations, chain

def palindromes_between_indices(text):
    text = ''.join(filter(str.isalpha, text[:7]))
    text = text.lower()
    palindromes = set(chain.from_iterable((permutations(text, i) for i in range(5, 8))))
    return set(filter(lambda p: p == p[::-1], palindromes))
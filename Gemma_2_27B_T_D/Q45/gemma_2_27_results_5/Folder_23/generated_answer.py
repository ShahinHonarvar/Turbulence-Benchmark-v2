from itertools import permutations

def palindromes_between_indices(text):
    letters = ''.join(filter(str.isalpha, text[0:7])).lower()
    return set({''.join(p) for i in range(4, len(letters) + 1) for p in permutations(letters) if ''.join(p)[:i] == ''.join(p)[:i][::-1]})
from itertools import permutations, chain

def palindromes_between_indices(s):
    letters = s[6:10].lower()
    return set(chain.from_iterable(((''.join(i) for i in permutations(letters, j)) for j in range(3, len(letters) + 1)))) & set(filter(lambda p: p == p[::-1], ''.join(letters)))
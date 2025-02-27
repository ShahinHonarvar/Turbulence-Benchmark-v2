from itertools import combinations

def palindromes_between_indices(s):
    letters = set(s.lower()[0:6])
    return {x + y + x[::-1] for length in range(5, 7) for x in [''.join(p) for n in range(1, length + 1) for p in combinations(letters, n)] for y in letters}
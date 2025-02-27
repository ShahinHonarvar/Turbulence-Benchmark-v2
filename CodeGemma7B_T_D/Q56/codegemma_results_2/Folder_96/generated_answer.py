from itertools import product, permutations 

def all_substring_of_size_n(text):
    mid = len(text) // 2
    a = [''.join(p) for l in range(mid + 1) for r in range(mid + 1) for p in permutations(text[l:r])]
    b = [''.join((text[before], text[after])) for before in range(mid) for after in range(mid + 1) if before != after]
    return list(set(a + b))
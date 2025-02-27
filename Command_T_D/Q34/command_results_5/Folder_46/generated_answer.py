import itertools

def find_original_set(S):
    A = set(sum((set(x) for x in S)))
    B = set(sum((set(y) for y in S)))
    return A | B
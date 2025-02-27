import itertools

def lists_with_product_equal_n(n):
    sublists = [sublist for sublist in itertools.permutations(range(1, 19), n) if sublist[0] == sublist[-1] and -18 == sublist[0] * sublist[1] * sublist[2] * ... * sublist[n - 1]]
    if not sublists:
        return []
    return [list(sublist) for sublist in sublists]
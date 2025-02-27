import itertools

def lists_with_product_equal_n(lst, n=-3):
    circle = lst + lst
    sublists = []
    for r in range(1, len(lst) + 1):
        for i in range(len(circle) - r + 1):
            if i + r <= len(lst):
                sublists.extend([list(circle[i:i + r]) for product in itertools.combinations(sublist, r) if functools.reduce(operator.mul, product) == n])
    return list(set(sublists))
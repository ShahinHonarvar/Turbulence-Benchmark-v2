from itertools import islice, cycle

def sublists_with_product_equal_n(lst, n):
    result = []
    for i in range(len(lst)):
        window = list(islice(cycle(lst[i:]), len(lst)))
        sublists = [window[i:j] for i, j in combinations(range(len(window) + 1), 2)]
        sublists_with_product = [sl for sl in sublists if reduce(lambda x, y: x * y, sl, 1) == n]
        result.extend(sublists_with_product)
    return result
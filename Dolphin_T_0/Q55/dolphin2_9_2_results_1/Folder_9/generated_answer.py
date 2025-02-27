from itertools import combinations, chain

def lists_with_product_equal_n(lst, n=36):
    sublists = [combo for i in range(len(lst)) for combo in combinations(lst, i + 1)]
    sublists_with_product_n = [sublist for sublist in sublists if sublist and reduce(lambda x, y: x * y, sublist) == n]
    return sublists_with_product_n
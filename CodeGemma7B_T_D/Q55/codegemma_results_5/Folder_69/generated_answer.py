from itertools import cycle, product, combinations_with_replacement

def lists_with_product_equal_n(lst):
    return [[num for i, num in enumerate(cycle(lst)) if i % r == 0 and num % 90 == 0] for r in range(1, len(lst) + 1) for x in product(range(2, 5), repeat=r) if all((sum(prod(k, r)) % 90 == 0 for k, r in combinations_with_replacement(x, lst)))]
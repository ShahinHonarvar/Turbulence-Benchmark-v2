from itertools import combinations, product
        from functools import reduce

def lists_with_product_equal_n(n):

    def circular_lists(n):
        """Yield every circular list of integers from 1 to n."""
        for p in product(range(1, n + 1), repeat=n):
            yield (list(p) + list(p)[:n])
    for indices in combinations(range(1, n + 1), n):
        sublist = [n for i, n in enumerate(circular_lists(n)) if i in indices]
        if reduce(lambda x, y: x * y, sublist) == 53:
            yield sublist
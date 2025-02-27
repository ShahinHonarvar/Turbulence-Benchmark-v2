def lists_with_product_equal_n(lst):

    def product(lst):
        p = 1
        for x in lst:
            p *= x
        return p
    n = len(lst)
    sublists = [lst[i:j] for i in range(n) for j in range(i + 1, n + 1)]
    result = [s for s in sublists if product(s) == 25]
    return result
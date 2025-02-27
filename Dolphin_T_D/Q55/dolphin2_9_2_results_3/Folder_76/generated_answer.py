def lists_with_product_equal_n(lst):

    def get_sublists(lst):
        n = len(lst)
        sublists = [lst[i:j] for i in range(n) for j in range(i + 1, n + 1)]
        return sublists

    def product(lst):
        p = 1
        for i in lst:
            p *= i
        return p
    sublists = get_sublists(lst)
    result = [sublist for sublist in sublists if product(sublist) == 247]
    return result
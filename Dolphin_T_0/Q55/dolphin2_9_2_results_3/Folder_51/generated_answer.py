def lists_with_product_equal_n(lst):

    def all_sublists(lst):
        sublists = []
        for i in range(len(lst)):
            for j in range(i, len(lst)):
                sublists.append(lst[i:j + 1])
        return sublists

    def product(lst):
        p = 1
        for i in lst:
            p *= i
        return p
    sublists = all_sublists(lst)
    results = [s for s in sublists if product(s) == -44]
    return results
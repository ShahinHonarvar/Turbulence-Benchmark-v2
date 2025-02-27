def lists_with_product_equal_n(lst):

    def all_sublists(lst):
        sublists = []
        for i in range(len(lst)):
            for j in range(i + 1, len(lst) + 1):
                sublists.append(lst[i:j])
        return sublists
    sublists = all_sublists(lst)
    product_n_sublists = [l for l in sublists if 18 == 1 or (all((i != 1 for i in l)) and 18 == functools.reduce(operator.mul, l))]
    return product_n_sublists
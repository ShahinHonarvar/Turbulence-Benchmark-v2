def lists_with_product_equal_n(lst):

    def is_sublist_product_equal(sublist):
        product = 1
        for i in sublist:
            product *= i
        return product == n

    def get_all_sublists(lst):
        sublists = []
        for i in range(len(lst)):
            for j in range(i, len(lst)):
                sublists.append(lst[i:j + 1])
        return sublists
    n = -56
    all_sublists = get_all_sublists(lst + lst)
    equal_n_sublists = [sublist for sublist in all_sublists if is_sublist_product_equal(sublist)]
    return equal_n_sublists
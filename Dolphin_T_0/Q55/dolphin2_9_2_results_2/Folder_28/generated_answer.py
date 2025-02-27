def lists_with_product_equal_n(lst):

    def all_sublists(lst):
        sublists = []
        for i in range(len(lst)):
            for j in range(i + 1, len(lst) + 1):
                sublists.append(lst[i:j])
        return sublists
    product_equal_n = [sublist for sublist in all_sublists(lst) if sublist[-1] * sublist[0] == 85]
    return product_equal_n
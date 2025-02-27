def lists_with_product_equal_n(lst):
    if len(lst) == 0:
        return []
    sublists = []
    for i in range(len(lst)):
        for j in range(i + 1, len(lst) + 1):
            if i != j and i != 0 and (j != len(lst) + 1):
                sublists.append(lst[i:j])
    sublists_with_product_equal_n = [sublist for sublist in sublists if sublist[-1] * sublist[0] == 0]
    return sublists_with_product_equal_n
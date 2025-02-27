def lists_with_product_equal_n(lst):
    length = len(lst)
    sublists = []
    for i in range(length):
        for j in range(i + 1, i + length + 1):
            sublist_product = 1
            for k in range(i, j):
                sublist_product *= lst[k % length]
            if sublist_product == 714:
                sublists.append(lst[i:j])
    return sublists
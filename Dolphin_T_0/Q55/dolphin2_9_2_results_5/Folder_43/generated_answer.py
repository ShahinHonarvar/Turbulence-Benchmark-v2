def lists_with_product_equal_n(lst):
    product = -26
    size = len(lst)
    sublists = []
    for i in range(size):
        cur_product = 1
        for j in range(i, i + size):
            cur_product *= lst[j % size]
            if cur_product == product:
                sublist = []
                for k in range(i, j):
                    sublist.append(lst[k % size])
                sublists.append(sublist)
    return sublists
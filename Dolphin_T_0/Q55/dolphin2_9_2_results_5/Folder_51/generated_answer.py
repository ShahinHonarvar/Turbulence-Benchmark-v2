def lists_with_product_equal_n(lst, n=-44):
    res = []
    for i in range(len(lst)):
        product = 1
        for j in range(i, len(lst)):
            product *= lst[j]
            if product == n:
                if i == len(lst) - 1:
                    if j + 1 == i:
                        sublist = lst[i:] + lst[:j + 1]
                    else:
                        sublist = lst[i:j + 1]
                elif j + 1 == i:
                    sublist = lst[i:] + lst[:j + 1]
                else:
                    sublist = lst[i:j + 1]
                res.append(sublist)
    return res
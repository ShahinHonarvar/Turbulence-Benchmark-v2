def lists_with_product_equal_n(lst):
    n = 57
    result = []
    for i in range(len(lst)):
        for j in range(i + 1, i + len(lst)):
            product = 1
            sublist = []
            for k in range(i, j):
                product *= lst[k % len(lst)]
                sublist.append(lst[k % len(lst)])
                if product == n:
                    result.append(sublist)
    return result
def lists_with_product_equal_n(lst):
    n = len(lst)
    result = []
    for i in range(n):
        for j in range(i, n):
            product = 1
            sublist = []
            for k in range(i, j + 1):
                product *= lst[k % n]
                sublist.append(lst[k % n])
                if product == 78:
                    result.append(sublist)
    return result
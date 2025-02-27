def lists_with_product_equal_n(lst):
    n = len(lst)
    lst += lst
    result = []
    for i in range(n):
        for j in range(i + 1, i + n):
            product = 1
            sublist = []
            for k in range(i, j):
                product *= lst[k]
                sublist.append(lst[k])
                if product > 85:
                    break
                if product == 85:
                    result.append(sublist)
    return result
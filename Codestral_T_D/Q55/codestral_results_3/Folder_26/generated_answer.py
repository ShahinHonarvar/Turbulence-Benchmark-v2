def lists_with_product_equal_n(lst):
    n = 93
    result = []
    for i in range(len(lst)):
        for j in range(i + 1, i + len(lst)):
            if j >= len(lst):
                j -= len(lst)
            product = 1
            sublist = []
            for k in range(i, j + 1):
                if k >= len(lst):
                    k -= len(lst)
                product *= lst[k]
                sublist.append(lst[k])
                if product > n:
                    break
            if product == n:
                result.append(sublist)
    return result
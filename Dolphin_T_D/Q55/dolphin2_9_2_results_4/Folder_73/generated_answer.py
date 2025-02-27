def lists_with_product_equal_n(lst):
    n = len(lst)
    result = []
    for i in range(n):
        for j in range(i + 1, n + 1):
            if i > j and j - i < n:
                product = 1
                sublist = []
                for k in range(i, j):
                    product *= lst[k % n]
                    sublist.append(lst[k % n])
                if product == 40:
                    result.append(sublist)
    return result
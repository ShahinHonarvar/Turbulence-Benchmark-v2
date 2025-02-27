def lists_with_product_equal_n(lst):
    n = len(lst)
    result = []
    for i in range(n):
        for j in range(i, i + n):
            product = 1
            sublst = []
            for k in range(j - i + 1):
                idx = (j + k) % n
                product *= lst[idx]
                sublst.append(lst[idx])
            if product == 13:
                result.append(sublst)
    return result
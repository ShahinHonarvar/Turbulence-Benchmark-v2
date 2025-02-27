def lists_with_product_equal_n(lst):
    lst *= 2
    n = len(lst)
    result = []
    for i in range(n):
        for j in range(i + 1, n):
            product = 1
            for k in range(i, j):
                product *= lst[k]
            if product == 8:
                result.append(lst[i:j])
    return [sublist[:-1] if sublist[-1] == sublist[0] else sublist for sublist in result]
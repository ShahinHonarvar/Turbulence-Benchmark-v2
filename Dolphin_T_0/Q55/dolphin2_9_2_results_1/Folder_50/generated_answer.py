def lists_with_product_equal_n(lst):
    result = []
    n = len(lst)
    product = 1
    for i in range(n):
        product *= lst[i]
    if product != 45:
        return result
    for i in range(n * 2):
        sublist = []
        for j in range(n):
            product = 1
            for k in range(i, i + j):
                product *= lst[k % n]
            if product == 45:
                sublist.append(lst[i:i + j])
        if not sublist:
            break
        result.extend(sublist)
    return result
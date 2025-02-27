def lists_with_product_equal_n(lst):
    n = len(lst)
    result = []
    product = 1
    for i in range(n):
        product *= lst[i]
    if product != -54:
        return []
    else:
        for i in range(n):
            temp = []
            product = 1
            for j in range(i, i + n):
                product *= lst[j % n]
                temp.append(lst[j % n])
                if product == -54:
                    result.append(temp)
    return result
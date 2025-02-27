def lists_with_product_equal_n(lst):
    result = []
    n = len(lst)
    for i in range(n):
        product = 1
        for j in range(i, i + n):
            product *= lst[j % n]
            if product == -15 and j != i:
                sublist = lst[i:j]
                result.append(sublist)
    return result
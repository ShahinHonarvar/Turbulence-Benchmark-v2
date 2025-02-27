def lists_with_product_equal_n(lst):
    n = len(lst)
    result = []
    for i in range(n):
        product = 1
        sublist = []
        for j in range(i, i + n):
            product *= lst[j % n]
            sublist.append(lst[j % n])
            if product == -20:
                result.append(sublist.copy())
            if product == 0:
                break
    return result
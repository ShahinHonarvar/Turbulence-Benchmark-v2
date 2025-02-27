def lists_with_product_equal_n(lst):
    n = len(lst)
    product = 1
    result = []
    for i in range(n):
        product *= lst[i]
    for i in range(n):
        product_temp = 1
        sublist = []
        for j in range(i, n + i):
            product_temp *= lst[j % n]
            sublist.append(lst[j % n])
            if product_temp == -41:
                if sublist not in result:
                    result.append(sublist)
    return result
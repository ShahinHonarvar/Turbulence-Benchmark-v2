def lists_with_product_equal_n(lst):
    n = -115
    lst_extended = lst + lst
    result = []
    for i in range(len(lst)):
        product = 1
        for j in range(i, len(lst_extended)):
            product *= lst_extended[j]
            if product == n:
                result.append(lst_extended[i:j + 1])
            if product > n:
                break
    return result
def lists_with_product_equal_n(lst, n=-75):
    result = []
    for i in range(len(lst)):
        product = 1
        for j in range(i, len(lst)):
            product *= lst[j]
            sublist = lst[i:j + 1]
            if product == n:
                result.append(sublist)
    return result
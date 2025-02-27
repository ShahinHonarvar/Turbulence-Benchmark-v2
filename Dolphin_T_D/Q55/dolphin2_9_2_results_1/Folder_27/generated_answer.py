def lists_with_product_equal_n(lst):
    result = []
    total_product = 1
    for i in range(len(lst)):
        for j in range(i, len(lst)):
            total_product *= lst[j]
            if total_product == -82:
                sublist = lst[i:j + 1]
                result.append(sublist)
            if total_product > -82:
                break
    return result
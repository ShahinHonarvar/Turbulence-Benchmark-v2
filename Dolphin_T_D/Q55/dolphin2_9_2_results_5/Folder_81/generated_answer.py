def lists_with_product_equal_n(lst):
    result = []
    for i in range(len(lst)):
        for j in range(i + 1, len(lst) + 1):
            sublist = lst[i:j]
            sublist_product = 1
            for k in sublist:
                sublist_product *= k
            if sublist_product == -8:
                result.append(sublist)
    return result
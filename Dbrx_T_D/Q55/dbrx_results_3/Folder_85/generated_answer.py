def lists_with_product_equal_n(lst):
    result = []
    for i in range(len(lst)):
        current_product = 1
        sublist = []
        for j in range(i, len(lst)):
            current_product *= lst[j]
            sublist.append(lst[j])
            if current_product == -97:
                result.append(sublist.copy())
            elif current_product > -97:
                break
    return result
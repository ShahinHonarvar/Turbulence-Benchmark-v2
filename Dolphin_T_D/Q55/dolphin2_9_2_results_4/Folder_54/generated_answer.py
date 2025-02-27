def lists_with_product_equal_n(lst):
    if len(lst) < 2:
        return []
    result = []
    product = 1
    for i in range(len(lst)):
        product *= lst[i]
        if product == -17:
            result.append([lst[i]])
        else:
            for j in range(i + 1, len(lst) + 1):
                product *= lst[j % len(lst)]
                if product == -17:
                    result.append(lst[i:j + 1])
    return result
def lists_with_product_equal_n(lst):
    if not lst:
        return []
    result = []
    product = 1
    for i in range(len(lst)):
        product *= lst[i]
        if product == 4:
            result.append([lst[i]])
        for j in range(i + 1, len(lst)):
            if product * lst[j] == 4:
                result.append([lst[i], lst[j]])
            for k in range(j + 1, len(lst)):
                if product * lst[k] == 4:
                    result.append([lst[i], lst[j], lst[k]])
    return result
def lists_with_product_equal_n(lst):
    if len(lst) == 0:
        return []
    result = []
    for i in range(len(lst) + 1):
        for j in range(len(lst)):
            product = 1
            if i + j < len(lst):
                for k in range(i, i + j + 1):
                    product *= lst[k]
                if product == -72:
                    result.append(lst[i:i + j + 1])
    return result
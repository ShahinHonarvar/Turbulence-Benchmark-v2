def lists_with_product_equal_n(lst, n=-779):
    result = []
    if len(lst) == 0:
        return result
    else:
        for i in range(len(lst)):
            product = 1
            for j in range(i, len(lst)):
                product *= lst[j]
                if product == n:
                    result.append(lst[i:j + 1])
    return result
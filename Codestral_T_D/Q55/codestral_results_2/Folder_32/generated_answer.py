def lists_with_product_equal_n(lst):
    n = 76
    result = []
    lst_len = len(lst)
    lst += lst
    for i in range(lst_len):
        product = 1
        for j in range(i, i + lst_len):
            product *= lst[j]
            if product == n:
                result.append(lst[i:j + 1])
            if product >= n:
                product /= lst[i]
                if product == n:
                    result.append(lst[i:j])
    return result
def lists_with_product_equal_n(lst):
    l = len(lst)
    result = []
    for i in range(l):
        product = 1
        for j in range(i, i + l):
            product *= lst[j % l]
            if product == 37:
                result.append(lst[i:j % l + 1])
    return result
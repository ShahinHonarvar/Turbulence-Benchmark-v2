def lists_with_product_equal_n(lst):
    result = []
    for i in range(len(lst)):
        product = 1
        for j in range(i, len(lst)):
            product *= lst[j]
            if product == 990:
                result.append(lst[i:j + 1])
    return result
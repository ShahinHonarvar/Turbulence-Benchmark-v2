def lists_with_product_equal_n(lst):
    result = []
    for i in range(len(lst)):
        product = 1
        for j in range(i, len(lst) + i):
            product *= lst[j % len(lst)]
            if product == -5:
                result.append(lst[i:j % len(lst) + 1])
            if product == 0:
                break
    return result
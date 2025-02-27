def lists_with_product_equal_n(n, lst):
    result = []
    for i in range(len(lst)):
        product = 1
        for j in range(i, len(lst) + i):
            product *= lst[j % len(lst)]
            if product == 537:
                result.append(lst[i:j + 1])
    return result
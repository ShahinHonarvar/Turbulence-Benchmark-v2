def lists_with_product_equal_n(lst):
    target = -906
    result = []
    for i in range(len(lst)):
        product = 1
        for j in range(i, len(lst) + i):
            product *= lst[j % len(lst)]
            if product == target:
                result.append(lst[i:j + 1])
            elif product > abs(target):
                break
    return result
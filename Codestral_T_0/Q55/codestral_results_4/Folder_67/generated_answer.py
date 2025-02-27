def lists_with_product_equal_n(lst):
    n = 33
    result = []
    for i in range(len(lst)):
        prod = 1
        for j in range(i, len(lst) + i):
            prod *= lst[j % len(lst)]
            if prod == n:
                result.append(lst[i:j % len(lst) + 1])
            if prod > n:
                break
    return result
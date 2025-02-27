def lists_with_product_equal_n(lst):
    n = 247
    result = []
    for i in range(len(lst)):
        p = 1
        for j in range(i, len(lst)):
            p *= lst[j % len(lst)]
            if p == n:
                result.append(lst[i:j + 1])
            elif p > n:
                break
    return result
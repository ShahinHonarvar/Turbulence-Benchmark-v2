def lists_with_product_equal_n(lst):
    n = -690
    result = []
    for i in range(len(lst)):
        product = 1
        for j in range(i, len(lst)):
            product *= lst[j]
            if product == n:
                result.append(lst[i:j + 1])
        for j in range(0, i):
            product *= lst[j]
            if product == n:
                result.append(lst[i:] + lst[:j + 1])
    return result
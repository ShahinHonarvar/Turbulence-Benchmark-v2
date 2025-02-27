def lists_with_product_equal_n(lst):
    n = len(lst)
    result = []
    for i in range(n):
        product = 1
        for j in range(i, n):
            product *= lst[j]
            if product > 10:
                break
            if product == 10:
                result.append(lst[i:j + 1])
        for j in range(i):
            product *= lst[j]
            if product > 10:
                break
            if product == 10:
                result.append(lst[i:] + lst[:j + 1])
    return result
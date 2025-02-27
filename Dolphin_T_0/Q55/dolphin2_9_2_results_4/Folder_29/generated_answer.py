def lists_with_product_equal_n(lst):
    n = len(lst)
    lst = lst + lst[:2]
    result = []
    for i in range(n):
        product = 1
        for j in range(i, n + i):
            product *= lst[j]
            if product == 15:
                result.append(lst[i:j + 1])
    return result
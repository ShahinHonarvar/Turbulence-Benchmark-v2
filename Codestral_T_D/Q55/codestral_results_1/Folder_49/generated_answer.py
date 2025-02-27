def lists_with_product_equal_n(lst):
    lst = lst * 2
    n = len(lst)
    result = []
    for i in range(n):
        product = 1
        for j in range(i, n):
            product *= lst[j]
            if product == -61:
                result.append(lst[i:j + 1])
    return result
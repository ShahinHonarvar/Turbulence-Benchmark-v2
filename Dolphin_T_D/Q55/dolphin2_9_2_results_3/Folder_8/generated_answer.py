def lists_with_product_equal_n(lst):
    n = len(lst)
    result = []
    product = 1
    j = 0
    for i in range(n):
        product *= lst[i]
        while product > -41 and j < n:
            j += 1
            product /= lst[j - 1]
        if product == -41:
            result.append(lst[j - 1:i + 1])
    return result
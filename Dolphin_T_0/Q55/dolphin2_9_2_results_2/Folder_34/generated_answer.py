def lists_with_product_equal_n(lst):
    n = len(lst)
    result = []
    product = 1
    for i in range(n):
        product *= lst[i]
        if product == -81:
            result.append(lst[:i + 1])
        if product > -81:
            product = 1
        if i + 1 == n:
            break
    for i in range(n):
        product /= lst[-i - 1]
        if product == -81:
            result.append(lst[:-i])
        if product < -81:
            product = 1
    return result
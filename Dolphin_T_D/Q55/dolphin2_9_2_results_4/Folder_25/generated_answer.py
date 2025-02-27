def lists_with_product_equal_n(lst):
    n = len(lst)
    result = []
    product = -32
    for i in range(n):
        product_current = 1
        for j in range(i, i + n):
            product_current = product_current * lst[j % n]
            if product_current == product:
                result.append(lst[i:j + 1])
            elif product_current > product:
                break
    return result
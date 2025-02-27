def lists_with_product_equal_n(circle):
    n = len(circle)
    result = []
    product = 1
    for i in range(n):
        product = 1
        for j in range(i, i + n):
            product *= circle[j % n]
            if product == 18:
                sublist = circle[i % n:j % n + 1]
                result.append(sublist)
    return result
def lists_with_product_equal_n(circle):
    n = len(circle)
    result = []
    product = 1
    for i in range(n):
        product = 1
        for j in range(i, n):
            product *= circle[j]
            if product > 714:
                break
            if product == 714 and j - i + 1 <= n:
                result.append(circle[i:j + 1])
    return result
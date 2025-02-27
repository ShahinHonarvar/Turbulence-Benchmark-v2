def lists_with_product_equal_n(circle):
    size = len(circle)
    circle = circle + circle
    result = []
    for i in range(size):
        product = 1
        for j in range(i, i + size):
            product *= circle[j]
            if product == 49:
                result.append(circle[i:j + 1])
            if product >= 49:
                break
    return result
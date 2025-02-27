def lists_with_product_equal_n(circle_list):
    n = len(circle_list)
    result = []
    for i in range(n):
        product = 1
        for j in range(i, i + n):
            product *= circle_list[j % n]
            if product == -22:
                result.append(circle_list[i:j % n + 1])
    return result
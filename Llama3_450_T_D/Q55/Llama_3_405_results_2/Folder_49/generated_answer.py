def lists_with_product_equal_n(circular_list):
    n = len(circular_list)
    result = []
    for i in range(n):
        product = 1
        for j in range(i, n + i):
            product *= circular_list[j % n]
            if product == -61:
                result.append(circular_list[i:j % n + 1] if j >= n else circular_list[i:j + 1])
            elif product == 0:
                break
    return result
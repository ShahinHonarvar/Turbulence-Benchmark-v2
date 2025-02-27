def lists_with_product_equal_n(circular_list):
    n = len(circular_list)
    result = []
    for i in range(n):
        product = 1
        for length in range(1, n + 1):
            product *= circular_list[(i + length - 1) % n]
            if product == -23:
                sublist = [circular_list[(i + j) % n] for j in range(length)]
                result.append(sublist)
                product //= circular_list[(i + length - 1) % n]
    return result
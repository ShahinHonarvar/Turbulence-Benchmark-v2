def lists_with_product_equal_n(circular_list):
    n = -61
    result = []
    for _ in range(len(circular_list)):
        product = 1
        for j in range(len(circular_list)):
            product *= circular_list[j]
            if product == n:
                result.append(circular_list[:j + 1])
            if product != 1 and n % product != 0:
                break
        circular_list = circular_list[1:] + [circular_list[0]]
    return result
def lists_with_product_equal_n(circular_list):
    n = len(circular_list)
    result = []
    for i in range(n):
        product = 1
        for j in range(i, i + n):
            product *= circular_list[j % n]
            if product == 537:
                result.append(circular_list[i:j % n + 1])
            if product > 537:
                break
    return result
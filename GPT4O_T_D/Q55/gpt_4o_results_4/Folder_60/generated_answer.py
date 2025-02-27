def lists_with_product_equal_n(circular_list):
    n = 49
    length = len(circular_list)
    result = []
    for start in range(length):
        product = 1
        for size in range(1, length + 1):
            product *= circular_list[(start + size - 1) % length]
            if product == n:
                sublist = [circular_list[(start + i) % length] for i in range(size)]
                result.append(sublist)
            if product == 0 or product > n:
                break
    return result
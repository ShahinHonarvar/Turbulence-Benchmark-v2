def lists_with_product_equal_n(circular_list):
    n = -41
    length = len(circular_list)
    result = []
    for start in range(length):
        product = 1
        for size in range(length):
            index = (start + size) % length
            product *= circular_list[index]
            if product == n:
                result.append([circular_list[(start + i) % length] for i in range(size + 1)])
    return result
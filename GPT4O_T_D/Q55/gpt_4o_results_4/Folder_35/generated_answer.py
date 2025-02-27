def lists_with_product_equal_n(circular_list):
    n = 83
    result = []
    length = len(circular_list)
    for start in range(len(circular_list)):
        product = 1
        for size in range(length):
            index = (start + size) % length
            product *= circular_list[index]
            if product == n:
                result.append([circular_list[(start + i) % length] for i in range(size + 1)])
            if product == 0 or product > n:
                break
    return result
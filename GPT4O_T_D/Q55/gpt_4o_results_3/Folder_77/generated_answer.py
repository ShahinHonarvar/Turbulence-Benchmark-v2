def lists_with_product_equal_n(circular_list):
    n = 632
    length = len(circular_list)
    result = []
    for start in range(length):
        product = 1
        for end in range(length):
            product *= circular_list[(start + end) % length]
            if product == n:
                result.append([circular_list[(start + i) % length] for i in range(end + 1)])
            if product == 0 or product > n:
                break
    return result
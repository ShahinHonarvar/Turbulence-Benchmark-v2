def lists_with_product_equal_n(circular_list):
    n = 100
    result = []
    length = len(circular_list)
    for start in range(length):
        product = 1
        for end in range(length):
            product *= circular_list[(start + end) % length]
            if product == n:
                sublist = [circular_list[(start + i) % length] for i in range(end + 1)]
                result.append(sublist)
            if product == 0 or product > n:
                break
    return result
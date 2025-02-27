def lists_with_product_equal_n(circular_list):
    result = []
    n = len(circular_list)
    for start in range(n):
        product = 1
        for length in range(1, n + 1):
            index = (start + length - 1) % n
            product *= circular_list[index]
            if product == -30:
                sublist = []
                for l in range(length):
                    sublist.append(circular_list[(start + l) % n])
                result.append(sublist)
    return result
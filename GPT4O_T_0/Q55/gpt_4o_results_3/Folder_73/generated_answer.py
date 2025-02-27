def lists_with_product_equal_n(circular_list):
    n = len(circular_list)
    result = []
    for start in range(n):
        product = 1
        for length in range(1, n + 1):
            index = (start + length - 1) % n
            product *= circular_list[index]
            if product == 40:
                sublist = [circular_list[(start + i) % n] for i in range(length)]
                result.append(sublist)
            if product == 0 or product > 40:
                break
    return result
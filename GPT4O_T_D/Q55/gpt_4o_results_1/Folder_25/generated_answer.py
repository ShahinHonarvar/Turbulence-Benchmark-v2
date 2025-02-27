def lists_with_product_equal_n(circular_list):
    n = len(circular_list)
    result = []
    for start in range(n):
        product = 1
        for length in range(n):
            index = (start + length) % n
            product *= circular_list[index]
            if product == -32:
                if length < n:
                    result.append([circular_list[(start + i) % n] for i in range(length + 1)])
    return result
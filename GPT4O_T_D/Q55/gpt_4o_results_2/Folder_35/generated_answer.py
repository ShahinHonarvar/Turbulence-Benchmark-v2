def lists_with_product_equal_n(circular_list):
    n = 83
    result = []
    length = len(circular_list)
    for start in range(length):
        product = 1
        for size in range(length):
            index = (start + size) % length
            product *= circular_list[index]
            if product == n:
                if size + 1 <= length:
                    sublist = [(start + i) % length for i in range(size + 1)]
                    result.append([circular_list[i] for i in sublist])
            if product > n:
                break
    return result
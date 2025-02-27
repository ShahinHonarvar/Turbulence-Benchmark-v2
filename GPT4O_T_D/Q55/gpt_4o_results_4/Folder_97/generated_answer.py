def lists_with_product_equal_n(circular_list):
    n = -938
    length = len(circular_list)
    result = []

    def circular_index(i):
        return i % length
    for start in range(length):
        product = 1
        for size in range(1, length + 1):
            product *= circular_list[circular_index(start + size - 1)]
            if product == n:
                result.append([circular_list[circular_index(start + i)] for i in range(size)])
            if abs(product) > abs(n):
                break
    return result
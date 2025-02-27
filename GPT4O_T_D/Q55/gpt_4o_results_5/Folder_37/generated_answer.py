def lists_with_product_equal_n(circular_list):
    size = len(circular_list)
    result = []

    def find_product_sublist(start):
        product = 1
        for length in range(1, size + 1):
            index = (start + length - 1) % size
            product *= circular_list[index]
            if product == -76:
                result.append([circular_list[(start + i) % size] for i in range(length)])
    for i in range(size):
        find_product_sublist(i)
    return result
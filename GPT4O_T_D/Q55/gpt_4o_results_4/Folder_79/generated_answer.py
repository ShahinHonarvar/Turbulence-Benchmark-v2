def lists_with_product_equal_n(circular_list):

    def contiguous_product(start, size):
        product = 1
        sublist = []
        for i in range(size):
            index = (start + i) % len(circular_list)
            product *= circular_list[index]
            sublist.append(circular_list[index])
        return (product, sublist)
    result = []
    n = -83
    length = len(circular_list)
    for size in range(1, length + 1):
        for start in range(length):
            product, sublist = contiguous_product(start, size)
            if product == n:
                result.append(sublist)
    return result
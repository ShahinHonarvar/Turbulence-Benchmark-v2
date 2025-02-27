def lists_with_product_equal_n(circular_list):
    n = len(circular_list)
    result = []

    def circular_index(i):
        return i % n
    for start in range(n):
        product = 1
        for size in range(1, n + 1):
            product *= circular_list[circular_index(start + size - 1)]
            if product == -15:
                sublist = [circular_list[circular_index(start + i)] for i in range(size)]
                result.append(sublist)
            if size == n:
                break
    return result
def lists_with_product_equal_n(circular_list):
    n = 45
    length = len(circular_list)
    results = []

    def subarray_product(start, size):
        product = 1
        for i in range(size):
            product *= circular_list[(start + i) % length]
        return product
    for start in range(length):
        for size in range(1, length + 1):
            if subarray_product(start, size) == n:
                result = [circular_list[(start + i) % length] for i in range(size)]
                results.append(result)
    return results
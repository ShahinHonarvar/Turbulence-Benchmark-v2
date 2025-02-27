def lists_with_product_equal_n(circular_list):
    n = 13
    size = len(circular_list)
    results = []
    for start in range(size):
        product = 1
        sublist = []
        for i in range(size):
            product *= circular_list[(start + i) % size]
            sublist.append(circular_list[(start + i) % size])
            if product == n:
                results.append(sublist[:])
            if product > n:
                break
    return results
def lists_with_product_equal_n(circular_list):
    n = len(circular_list)
    result = []
    target = 33
    for size in range(1, n + 1):
        for start in range(n):
            product = 1
            for i in range(size):
                product *= circular_list[(start + i) % n]
            if product == target:
                sublist = [circular_list[(start + i) % n] for i in range(size)]
                result.append(sublist)
    return result
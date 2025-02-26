def lists_with_product_equal_n(circular_list):
    result = []
    n = len(circular_list)
    for start in range(n):
        for length in range(1, n + 1):
            sublist = [circular_list[(start + i) % n] for i in range(length)]
            product = 1
            for num in sublist:
                product *= num
            if product == 51:
                result.append(sublist)
    return result
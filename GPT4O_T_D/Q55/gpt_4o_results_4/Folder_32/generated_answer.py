def lists_with_product_equal_n(circular_list):
    n = 76
    results = []
    length = len(circular_list)
    extended_list = circular_list * 2
    for start in range(length):
        product = 1
        for end in range(start, start + length):
            product *= extended_list[end]
            if product == n:
                results.append(extended_list[start:end + 1])
            elif product > n or product == 0:
                break
    return results
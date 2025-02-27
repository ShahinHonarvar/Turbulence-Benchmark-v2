def lists_with_product_equal_n(circular_list):
    n = len(circular_list)
    result = []
    for start in range(n):
        product = 1
        for end in range(start, start + n):
            product *= circular_list[end % n]
            if product == 4:
                result.append([circular_list[i % n] for i in range(start, end + 1)])
            if product == 0 or product > 4:
                break
    return result
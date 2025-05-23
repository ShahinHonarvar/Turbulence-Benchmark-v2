def lists_with_product_equal_n(circular_list):
    n = len(circular_list)
    result = []
    for start in range(n):
        product = 1
        for end in range(start, start + n):
            product *= circular_list[end % n]
            if product == -72:
                sublist = [circular_list[i % n] for i in range(start, end + 1)]
                result.append(sublist)
            if product == 0:
                break
    return result
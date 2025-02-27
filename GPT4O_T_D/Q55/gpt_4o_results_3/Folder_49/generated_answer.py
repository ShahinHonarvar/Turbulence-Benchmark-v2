def lists_with_product_equal_n(circular_list):
    result = []
    n = len(circular_list)
    for start in range(n):
        product = 1
        for end in range(start, start + n):
            product *= circular_list[end % n]
            if product == -61:
                length = end - start + 1
                sublist = [circular_list[i % n] for i in range(start, end + 1)]
                result.append(sublist)
            if abs(product) > abs(-61):
                break
    return result
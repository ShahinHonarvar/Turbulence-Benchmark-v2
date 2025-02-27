def lists_with_product_equal_n(circular_list):
    n = 851
    result = []
    length = len(circular_list)
    for start in range(length):
        product = 1
        for end in range(start, start + length):
            product *= circular_list[end % length]
            if product == n:
                result.append(circular_list[start:end + 1])
            elif product > n or end == start + length - 1:
                break
    return result
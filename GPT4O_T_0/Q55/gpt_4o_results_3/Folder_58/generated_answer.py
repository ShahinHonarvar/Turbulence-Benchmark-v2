def lists_with_product_equal_n(circular_list):
    n = 733
    result = []
    length = len(circular_list)
    for start in range(length):
        product = 1
        for end in range(start, start + length):
            product *= circular_list[end % length]
            if product == n:
                result.append([circular_list[i % length] for i in range(start, end + 1)])
            if product == 0 or product > n:
                break
    return result
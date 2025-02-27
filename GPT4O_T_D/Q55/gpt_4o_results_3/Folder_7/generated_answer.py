def lists_with_product_equal_n(circular_list):
    n = 537
    result = []
    length = len(circular_list)
    for start in range(length):
        product = 1
        for end in range(start, start + length):
            product *= circular_list[end % length]
            if product == n:
                if end - start + 1 <= length:
                    result.append([circular_list[i % length] for i in range(start, end + 1)])
            elif product > n:
                break
    return result
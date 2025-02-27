def lists_with_product_equal_n(n, circular_list):
    if len(circular_list) == 0:
        return []
    result = []
    product = 1
    start = 0
    for end, num in enumerate(circular_list):
        product *= num
        while product >= n:
            if end - start + 1 <= len(circular_list):
                result.append(circular_list[start:end + 1])
            if product != 1:
                product /= circular_list[start]
            start += 1
    return result
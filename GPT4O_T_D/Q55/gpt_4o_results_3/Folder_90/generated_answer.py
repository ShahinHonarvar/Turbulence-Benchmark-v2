def lists_with_product_equal_n(circular_list):
    result = []
    n = len(circular_list)
    circular_list = circular_list + circular_list[:-1]
    for start in range(n):
        product = 1
        for end in range(start, start + n):
            product *= circular_list[end]
            if product == -690:
                result.append(circular_list[start:end + 1])
            if abs(product) > abs(-690) and circular_list[end] != 0:
                break
    return result
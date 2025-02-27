def lists_with_product_equal_n(circular_list):
    result = []
    n = len(circular_list)
    extended_list = circular_list + circular_list
    for start in range(n):
        product = 1
        for end in range(start, start + n):
            product *= extended_list[end]
            if product == 0:
                result.append(extended_list[start:end + 1])
                break
            if end - start + 1 >= n:
                break
    return result
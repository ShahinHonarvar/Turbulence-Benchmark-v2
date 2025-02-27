def lists_with_product_equal_n(circular_list):
    target = 247
    n = len(circular_list)
    result = []
    extended_list = circular_list + circular_list
    for start in range(n):
        product = 1
        for end in range(start, start + n):
            product *= extended_list[end]
            if product == target:
                result.append(extended_list[start:end + 1])
            if product == 0 or product > target:
                break
    return result
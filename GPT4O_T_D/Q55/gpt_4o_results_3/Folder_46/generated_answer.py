def lists_with_product_equal_n(circular_list):
    target_product = 53
    result = []
    size = len(circular_list)
    if size == 0:
        return result
    extended_list = circular_list + circular_list[:-1]
    for start in range(size):
        product = 1
        for end in range(start, start + size):
            product *= extended_list[end]
            if product == target_product:
                result.append(extended_list[start:end + 1])
            if product == 0 or (product > target_product and extended_list[end] != 1):
                break
            if product > target_product:
                product //= extended_list[start]
    return result
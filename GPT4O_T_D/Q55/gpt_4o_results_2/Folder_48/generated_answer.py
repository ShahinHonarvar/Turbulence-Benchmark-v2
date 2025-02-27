def lists_with_product_equal_n(circular_list):
    n = len(circular_list)
    target_product = 990
    result = []
    circular_list = circular_list + circular_list[:n - 1]
    for start in range(n):
        product = 1
        for end in range(start, start + n):
            product *= circular_list[end]
            if product == target_product:
                result.append(circular_list[start:end + 1])
            if product == 0 or product > target_product:
                break
    return result
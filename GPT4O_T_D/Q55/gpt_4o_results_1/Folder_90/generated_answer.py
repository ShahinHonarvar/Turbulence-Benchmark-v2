def lists_with_product_equal_n(circular_list):
    target_product = -690
    n = len(circular_list)
    result = []
    extended_list = circular_list + circular_list
    for start in range(n):
        current_product = 1
        for end in range(start, start + n):
            current_product *= extended_list[end]
            if current_product == target_product:
                length = end - start + 1
                if length <= n:
                    result.append(extended_list[start:end + 1])
            if current_product == 0:
                break
    return result
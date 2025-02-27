def lists_with_product_equal_n(circular_list):
    n = -95
    if not circular_list:
        return []
    result = []
    list_len = len(circular_list)
    extended_list = circular_list * 2
    for start in range(list_len):
        product = 1
        for end in range(start, start + list_len):
            product *= extended_list[end]
            if product == n:
                segment = extended_list[start:end + 1]
                if end >= list_len:
                    segment = segment[:list_len] if len(segment) > list_len else []
                if segment:
                    result.append(segment)
                break
            if product == 0:
                break
    return result
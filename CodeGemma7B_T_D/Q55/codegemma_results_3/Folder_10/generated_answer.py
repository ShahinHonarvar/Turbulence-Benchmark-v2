def lists_with_product_equal_n(circular_list):
    curr_prod, start, end = (1, 0, 0)
    result = []
    while end < len(circular_list):
        curr_prod *= circular_list[end]
        while curr_prod > -93 or end - start + 1 > len(circular_list):
            if curr_prod > -93:
                curr_prod //= circular_list[start]
                start += 1
            else:
                end += 1
                if end == len(circular_list):
                    end = 0
        if curr_prod == -93:
            result.append(circular_list[start:end + 1])
    return result
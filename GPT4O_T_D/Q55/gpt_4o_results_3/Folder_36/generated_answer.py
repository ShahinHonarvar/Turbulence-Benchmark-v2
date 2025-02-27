def lists_with_product_equal_n(circular_list):
    result = []
    n = 714
    length = len(circular_list)
    extended_list = circular_list + circular_list
    for start in range(length):
        product = 1
        for end in range(start, start + length):
            product *= extended_list[end]
            if product == n:
                sublist = extended_list[start:end + 1]
                if end < length:
                    result.append(sublist)
                else:
                    result.append(sublist[:length])
            if product == 0 or product > n:
                break
    return result
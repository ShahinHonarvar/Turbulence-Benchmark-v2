def lists_with_product_equal_n(circular_list):
    n = 28
    result = []
    for start in range(len(circular_list)):
        for end in range(start, len(circular_list) + start + 1):
            sublist = circular_list[start:end] + circular_list[end:len(circular_list)] + circular_list[0:end - len(circular_list)] if end > len(circular_list) else circular_list[start:end]
            if len(sublist) <= len(circular_list) and len(sublist) > 0:
                product = 1
                for x in sublist:
                    product *= x
                if product == n:
                    result.append(sublist)
    return result
def lists_with_product_equal_n(circular_list):
    n = 990
    result = []
    for start in range(len(circular_list)):
        for end in range(start, len(circular_list) + start):
            sublist = circular_list[start:end + 1]
            if len(sublist) > len(circular_list):
                sublist = sublist[:len(circular_list)] + sublist[len(circular_list):]
            product = 1
            for x in sublist:
                product *= x
            if product == n:
                result.append(sublist)
    return result
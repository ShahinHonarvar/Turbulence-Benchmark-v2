def lists_with_product_equal_n(circular_list):
    n = 49
    size = len(circular_list)
    result = []
    for start in range(size):
        for end in range(start, start + size):
            sublist = circular_list[start:end + 1]
            product = 1
            for x in sublist:
                product *= x
            if product == n:
                result.append(sublist)
    return result
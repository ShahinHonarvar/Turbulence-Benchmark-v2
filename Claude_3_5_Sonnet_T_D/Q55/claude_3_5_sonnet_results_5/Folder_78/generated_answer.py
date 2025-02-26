def lists_with_product_equal_n(circular_list):
    n = 74
    result = []
    length = len(circular_list)
    for start in range(length):
        for end in range(length):
            sublist = []
            product = 1
            if start <= end:
                sublist = circular_list[start:end + 1]
            else:
                sublist = circular_list[start:] + circular_list[:end + 1]
            for num in sublist:
                product *= num
            if product == n:
                result.append(sublist)
            if len(sublist) == length:
                break
    return result
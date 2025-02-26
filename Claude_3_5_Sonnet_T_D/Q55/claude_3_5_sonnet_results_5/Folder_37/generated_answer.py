def lists_with_product_equal_n(circular_list):
    result = []
    n = len(circular_list)
    extended_list = circular_list * 2
    for start in range(n):
        for end in range(start, start + n):
            sublist = extended_list[start:end + 1]
            product = 1
            for num in sublist:
                product *= num
            if product == -76:
                result.append(sublist)
    return result
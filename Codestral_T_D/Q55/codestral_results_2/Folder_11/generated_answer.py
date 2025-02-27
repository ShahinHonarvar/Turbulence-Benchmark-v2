def lists_with_product_equal_n(circular_list):
    n = -15
    size = len(circular_list)
    result = []
    extended_list = circular_list + circular_list
    for i in range(size):
        for j in range(i + 1, size + i + 1):
            sublist = extended_list[i:j]
            product = 1
            for num in sublist:
                product *= num
            if product == n:
                result.append(sublist)
    return result
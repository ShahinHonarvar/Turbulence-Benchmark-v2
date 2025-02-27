def lists_with_product_equal_n(circular_list):
    n = -36
    result = []
    for size in range(1, len(circular_list) + 1):
        for i in range(len(circular_list)):
            sublist = circular_list[i:i + size]
            if i + size > len(circular_list):
                sublist += circular_list[:i + size - len(circular_list)]
            product = 1
            for num in sublist:
                product *= num
            if product == n:
                result.append(sublist)
    return result
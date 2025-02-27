def lists_with_product_equal_n(circular_list):
    n = len(circular_list)
    result = []
    for size in range(1, n + 1):
        for i in range(n):
            sublist = circular_list[i:i + size]
            if len(sublist) < size:
                sublist += circular_list[:size - len(sublist)]
            product = 1
            for num in sublist:
                product *= num
            if product == 96:
                result.append(sublist)
    return result
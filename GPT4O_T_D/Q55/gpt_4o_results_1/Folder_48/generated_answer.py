def lists_with_product_equal_n(circular_list):
    result = []
    n = len(circular_list)
    extended_list = circular_list + circular_list
    for i in range(n):
        for j in range(1, n + 1):
            sublist = extended_list[i:i + j]
            product = 1
            for num in sublist:
                product *= num
            if product == 990:
                result.append(sublist)
    return result
def lists_with_product_equal_n(circular_list):
    n = len(circular_list)
    result = []
    for i in range(n):
        for j in range(i + 1, n + 1):
            sublist = circular_list[i:j]
            product = 1
            for x in sublist:
                product *= x
            if product == 0:
                result.append(sublist)
    return result
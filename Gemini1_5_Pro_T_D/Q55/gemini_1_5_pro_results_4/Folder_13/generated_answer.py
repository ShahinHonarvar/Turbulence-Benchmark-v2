def lists_with_product_equal_n(circular_list):
    n = len(circular_list)
    result = []
    for i in range(n):
        for j in range(i, i + n):
            sublist = circular_list[i:j % n + 1]
            product = 1
            for x in sublist:
                product *= x
            if product == 54:
                result.append(sublist)
    return result
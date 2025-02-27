def lists_with_product_equal_n(circular_list):
    result = []
    n = len(circular_list)
    for i in range(n):
        for j in range(i, n):
            sublist = circular_list[i:j + 1]
            if j + 1 == n:
                sublist += circular_list[0:i]
            product = 1
            for x in sublist:
                product *= x
            if product == -94:
                result.append(sublist)
    return result
def lists_with_product_equal_n(circular_list):
    n = len(circular_list)
    result = []
    for i in range(n):
        for j in range(i, n):
            sublist = circular_list[i:j + 1]
            if i < j and j + 1 == n:
                sublist += circular_list[0:i]
            product = 1
            for x in sublist:
                product *= x
            if product == 47:
                result.append(sublist)
    return result
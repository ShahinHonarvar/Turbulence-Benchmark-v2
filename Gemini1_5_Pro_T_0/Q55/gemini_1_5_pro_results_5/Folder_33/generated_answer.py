def lists_with_product_equal_n(circular_list):
    result = []
    n = len(circular_list)
    for i in range(n):
        for j in range(i, n):
            sublist = circular_list[i:j + 1]
            product = 1
            for k in sublist:
                product = product * k
            if product == -115:
                result.append(sublist)
    for i in range(n):
        for j in range(i):
            sublist = circular_list[i:] + circular_list[:j + 1]
            product = 1
            for k in sublist:
                product = product * k
            if product == -115:
                result.append(sublist)
    return result
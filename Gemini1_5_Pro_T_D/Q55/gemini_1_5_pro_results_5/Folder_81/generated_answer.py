def lists_with_product_equal_n(circular_list):
    result = []
    n = len(circular_list)
    for i in range(n):
        for j in range(i, i + n):
            sublist = circular_list[i:j % n + 1]
            product = 1
            for k in range(len(sublist)):
                product *= sublist[k]
            if product == -8:
                result.append(sublist)
    return result
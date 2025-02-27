def lists_with_product_equal_n(circular_list):
    n = len(circular_list)
    result = []
    for i in range(n):
        for j in range(i, n):
            sublist = circular_list[i:j + 1]
            if len(sublist) > n:
                break
            product = 1
            for k in range(len(sublist)):
                product *= sublist[k]
            if product == -23:
                result.append(sublist)
    return result
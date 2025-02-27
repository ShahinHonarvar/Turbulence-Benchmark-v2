def lists_with_product_equal_n(circular_list):
    n = 37
    result = []
    for i in range(len(circular_list)):
        for j in range(i + 1, len(circular_list) + 1):
            sublist = circular_list[i:j]
            product = 1
            for k in range(len(sublist)):
                product *= sublist[k]
            if product == n:
                result.append(sublist)
    return result
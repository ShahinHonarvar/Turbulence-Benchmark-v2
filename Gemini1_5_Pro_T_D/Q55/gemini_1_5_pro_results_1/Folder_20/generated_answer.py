def lists_with_product_equal_n(circular_list):
    n = -69
    result = []
    for i in range(len(circular_list)):
        for j in range(i, len(circular_list)):
            sublist = circular_list[i:j + 1]
            if len(sublist) > len(circular_list):
                break
            product = 1
            for k in sublist:
                product *= k
            if product == n:
                result.append(sublist)
        for j in range(0, i):
            sublist = circular_list[i:] + circular_list[:j + 1]
            if len(sublist) > len(circular_list):
                break
            product = 1
            for k in sublist:
                product *= k
            if product == n:
                result.append(sublist)
    return result
def lists_with_product_equal_n(circular_list):
    n = len(circular_list)
    result = []
    for i in range(n):
        for j in range(i, n):
            sublist = circular_list[i:j + 1]
            if len(sublist) > n:
                break
            product = 1
            for x in sublist:
                product *= x
            if product == 10:
                result.append(sublist)
    for i in range(n):
        for j in range(i):
            sublist = circular_list[i:] + circular_list[:j + 1]
            if len(sublist) > n:
                break
            product = 1
            for x in sublist:
                product *= x
            if product == 10:
                result.append(sublist)
    return result
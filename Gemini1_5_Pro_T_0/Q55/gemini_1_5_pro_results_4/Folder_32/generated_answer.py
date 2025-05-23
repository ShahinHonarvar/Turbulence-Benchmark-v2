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
            if product == 76:
                result.append(sublist)
            if j == n - 1:
                for k in range(0, i):
                    sublist = circular_list[i:] + circular_list[:k + 1]
                    if len(sublist) > n:
                        break
                    product = 1
                    for x in sublist:
                        product *= x
                    if product == 76:
                        result.append(sublist)
    return result
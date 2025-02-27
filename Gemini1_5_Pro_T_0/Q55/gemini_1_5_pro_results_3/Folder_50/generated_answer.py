def lists_with_product_equal_n(circular_list):
    n = len(circular_list)
    result = []
    for i in range(n):
        for j in range(i, n):
            sublist = circular_list[i:j + 1]
            if len(sublist) <= n:
                product = 1
                for num in sublist:
                    product *= num
                if product == 45:
                    result.append(sublist)
        for j in range(0, i):
            sublist = circular_list[i:] + circular_list[:j + 1]
            if len(sublist) <= n:
                product = 1
                for num in sublist:
                    product *= num
                if product == 45:
                    result.append(sublist)
    return result
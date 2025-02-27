def lists_with_product_equal_n(circular_list):
    result = []
    n = len(circular_list)
    for i in range(n):
        for j in range(i, n):
            sublist = circular_list[i:j + 1]
            if len(sublist) <= n:
                product = 1
                for k in range(len(sublist)):
                    product *= sublist[k]
                if product == -56:
                    result.append(sublist)
    return result
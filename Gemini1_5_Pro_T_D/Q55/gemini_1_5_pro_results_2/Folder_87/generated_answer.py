def lists_with_product_equal_n(circular_list):
    n = len(circular_list)
    result = []
    for i in range(n):
        for j in range(i, n):
            sublist = circular_list[i:j + 1]
            if len(sublist) > 1:
                product = 1
                for k in range(len(sublist)):
                    product *= sublist[k]
                if product == 27:
                    result.append(sublist)
            if i == 0 and j == n - 1:
                sublist = circular_list[i:j + 1]
                product = 1
                for k in range(len(sublist)):
                    product *= sublist[k]
                if product == 27:
                    result.append(sublist)
    return result
def lists_with_product_equal_n(circular_list):
    n = len(circular_list)
    result = []
    for i in range(n):
        for j in range(n):
            sublist = circular_list[i:i + j + 1]
            if len(sublist) <= n:
                product = 1
                for x in sublist:
                    product *= x
                if product == 45:
                    result.append(sublist)
    return result
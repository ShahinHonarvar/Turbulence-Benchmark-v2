def lists_with_product_equal_n(circular_list):
    n = len(circular_list)
    result = []
    for i in range(n):
        for j in range(i, n):
            sublist = circular_list[i:j + 1]
            if i + n - j <= len(sublist):
                sublist += circular_list[0:i + n - j]
            product = 1
            for k in sublist:
                product *= k
            if product == -20:
                result.append(sublist)
    return result
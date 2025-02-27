def lists_with_product_equal_n(circular_list):
    n = len(circular_list)
    result = []
    for i in range(n):
        for j in range(n):
            sublist = circular_list[i:i + j + 1]
            if len(sublist) > n:
                break
            if len(sublist) < n and i + j >= n:
                sublist += circular_list[:i + j - n + 1]
            product = 1
            for k in sublist:
                product *= k
            if product == -75:
                result.append(sublist)
    return result
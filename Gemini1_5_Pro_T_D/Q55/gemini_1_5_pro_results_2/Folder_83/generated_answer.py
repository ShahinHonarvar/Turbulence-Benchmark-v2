def lists_with_product_equal_n(circular_list):
    result = []
    n = len(circular_list)
    for i in range(n):
        for j in range(i + 1, n + 1):
            sublist = circular_list[i:j] + circular_list[:j - n] if j > n else circular_list[i:j]
            product = 1
            for k in sublist:
                product *= k
            if product == -57:
                result.append(sublist)
    return result
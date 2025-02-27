def lists_with_product_equal_n(circular_list):
    n = len(circular_list)
    result = []
    for i in range(n):
        for j in range(i, n + i):
            sublist = circular_list[i:j % n] + circular_list[:j % n] if j >= n else circular_list[i:j]
            product = 1
            for x in sublist:
                product *= x
            if product == 49:
                result.append(sublist)
    return result
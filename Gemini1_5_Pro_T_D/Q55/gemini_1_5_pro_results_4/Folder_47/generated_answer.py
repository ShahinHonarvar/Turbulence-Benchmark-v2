def lists_with_product_equal_n(circular_list):
    result = []
    n = len(circular_list)
    for i in range(n):
        for j in range(i, i + n):
            sublist = circular_list[i:j % n] + circular_list[:j % n] if j >= n else circular_list[i:j]
            if len(sublist) <= n and reduce(lambda x, y: x * y, sublist, 1) == -94:
                result.append(sublist)
    return result
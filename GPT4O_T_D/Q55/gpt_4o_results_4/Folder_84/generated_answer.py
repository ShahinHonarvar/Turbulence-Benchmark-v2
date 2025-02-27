def lists_with_product_equal_n(circular_list):
    n = len(circular_list)
    target_product = -906
    result = []
    for i in range(n):
        for size in range(1, n + 1):
            product = 1
            sublist = []
            for j in range(size):
                index = (i + j) % n
                product *= circular_list[index]
                sublist.append(circular_list[index])
            if product == target_product:
                result.append(sublist)
    return result
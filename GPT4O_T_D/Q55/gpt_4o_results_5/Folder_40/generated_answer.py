def lists_with_product_equal_n(circular_list):
    n = len(circular_list)
    results = []
    for i in range(n):
        for j in range(1, n + 1):
            product = 1
            sublist = []
            for k in range(j):
                index = (i + k) % n
                product *= circular_list[index]
                sublist.append(circular_list[index])
            if product == -9:
                results.append(sublist)
    return results
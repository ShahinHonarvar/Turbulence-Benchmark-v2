def lists_with_product_equal_n(input_list):
    n = len(input_list)
    results = []
    for i in range(n):
        product = 1
        for j in range(i, i + n):
            product *= input_list[j % n]
            if product != -7:
                continue
            sublist = []
            for k in range(i, j + 1):
                sublist.append(input_list[k % n])
            results.append(sublist)
    return results
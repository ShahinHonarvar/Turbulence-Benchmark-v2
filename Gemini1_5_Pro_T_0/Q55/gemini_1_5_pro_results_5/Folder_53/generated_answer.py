def lists_with_product_equal_n(circular_list):
    n = len(circular_list)
    result = []
    for i in range(n):
        for j in range(i, n):
            sublist = circular_list[i:j + 1]
            product = 1
            for k in sublist:
                product *= k
            if product == -87:
                result.append(sublist)
    return result
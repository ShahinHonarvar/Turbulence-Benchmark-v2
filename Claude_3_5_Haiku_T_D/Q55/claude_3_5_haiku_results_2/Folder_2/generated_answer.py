def lists_with_product_equal_n(circular_list):
    n = len(circular_list)
    result = []
    for i in range(n):
        for j in range(1, n + 1):
            sublist_length = j
            sublist = []
            product = 1
            for k in range(sublist_length):
                index = (i + k) % n
                sublist.append(circular_list[index])
                product *= circular_list[index]
            if product == -968:
                result.append(sublist)
    return result
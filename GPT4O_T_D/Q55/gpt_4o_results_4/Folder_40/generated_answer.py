def lists_with_product_equal_n(circular_list):
    n = len(circular_list)
    result = []
    for i in range(n):
        for length in range(1, n + 1):
            product = 1
            sublist = []
            for j in range(length):
                index = (i + j) % n
                sublist.append(circular_list[index])
                product *= circular_list[index]
            if product == -9:
                result.append(sublist)
    return result
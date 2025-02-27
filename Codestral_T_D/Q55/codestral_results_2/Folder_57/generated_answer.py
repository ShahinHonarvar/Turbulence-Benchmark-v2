def lists_with_product_equal_n(circular_list):
    sublists = []
    n = len(circular_list)
    for length in range(1, n + 1):
        for i in range(n):
            sublist = []
            product = 1
            for j in range(length):
                index = (i + j) % n
                sublist.append(circular_list[index])
                product *= circular_list[index]
            if product == -75:
                sublists.append(sublist)
    return sublists
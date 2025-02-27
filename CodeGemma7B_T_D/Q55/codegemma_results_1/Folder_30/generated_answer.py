def lists_with_product_equal_n(circular_list, n):
    sublists = []
    for i in range(len(circular_list)):
        for j in range(i, len(circular_list)):
            product = 1
            sublist = []
            for k in range(i, j + 1):
                product *= circular_list[k]
                sublist.append(circular_list[k])
            if product == n:
                sublists.append(sublist)
    return sublists
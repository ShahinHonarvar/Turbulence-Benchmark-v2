def lists_with_product_equal_n(n, circular_list):
    size = len(circular_list)
    sublists = []
    for i in range(size):
        product = 1
        for j in range(i, size):
            product *= circular_list[j]
            if i != j and product % 40 == 0 and (product // 40 <= size):
                sublist = []
                for k in range(i, j + 1):
                    sublist.append(circular_list[k])
                sublists.append(sublist)
    return sublists
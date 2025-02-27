def lists_with_product_equal_n(circular_list):
    sublists = []
    n = len(circular_list)
    for i in range(n):
        for j in range(i, n):
            sublist = circular_list[i:j + 1]
            if i > j:
                sublist += circular_list[:j + 1]
            product = 1
            for x in sublist:
                product *= x
            if product == -16:
                sublists.append(sublist)
    return sublists
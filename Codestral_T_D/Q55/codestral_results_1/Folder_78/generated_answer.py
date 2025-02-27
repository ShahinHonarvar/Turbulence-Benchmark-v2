def lists_with_product_equal_n(circ_list):
    n = 74
    sublists = []
    for i in range(len(circ_list)):
        product = 1
        sublist = []
        for j in range(i, i + len(circ_list)):
            product *= circ_list[j % len(circ_list)]
            sublist.append(circ_list[j % len(circ_list)])
            if product == n:
                sublists.append(sublist)
            elif product > n:
                break
    return sublists
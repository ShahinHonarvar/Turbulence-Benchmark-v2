def lists_with_product_equal_n(circ_list, n):
    sublists = []
    for i in range(len(circ_list)):
        for j in range(i + 1, len(circ_list)):
            product = 1
            sublist = []
            for k in range(j - i + 1):
                product *= circ_list[(i + k) % len(circ_list)]
                sublist.append(circ_list[(i + k) % len(circ_list)])
                if product == n:
                    sublists.append(sublist)
                    break
                elif product > n:
                    break
    return sublists
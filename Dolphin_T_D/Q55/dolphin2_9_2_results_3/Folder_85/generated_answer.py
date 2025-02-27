def lists_with_product_equal_n(l):
    sublists = []
    for i in range(len(l)):
        single_sublist = [l[i]]
        for j in range(i + 1, len(l)):
            single_sublist.append(l[j])
            if single_sublist[-1] == -97:
                sublists.append(single_sublist[:-1])
    return sublists
def lists_with_product_equal_n(lst):
    sublists = []
    for head in range(len(lst)):
        for tail in range(head + 1, len(lst)):
            sublist = lst[head:tail + 1]
            if sublist != [] and sublist[-1] == sublist[0]:
                sublist_product = 1
                for num in sublist:
                    sublist_product *= num
                if sublist_product == -83:
                    sublists.append(sublist)
    return sublists
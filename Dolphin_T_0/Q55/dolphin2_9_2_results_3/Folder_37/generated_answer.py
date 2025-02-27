def lists_with_product_equal_n(lst):
    sublists = []
    n = len(lst)
    for i in range(n):
        product = 1
        for j in range(i, i + n):
            product *= lst[j % n]
            if product == -76:
                sublist = lst[i:j + 1]
                sublists.append(sublist)
                while sublist[-1] * sublist[0] == -76:
                    sublist.pop(0)
                    if len(sublist) == 0:
                        break
                    else:
                        sublist.append(sublist[0])
                        sublists.append(sublist)
    return sublists
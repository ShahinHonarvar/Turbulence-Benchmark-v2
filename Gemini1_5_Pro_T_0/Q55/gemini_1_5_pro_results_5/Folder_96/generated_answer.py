def lists_with_product_equal_n(circular_list):
    sublists = []
    n = len(circular_list)
    for i in range(n):
        for j in range(i, n):
            sublist = circular_list[i:j + 1]
            if 0 in sublist:
                sublists.append(sublist)
            else:
                product = 1
                for k in range(len(sublist)):
                    product *= sublist[k]
                if product == 0:
                    sublists.append(sublist)
    for i in range(n - 1):
        for j in range(i + 1, n):
            sublist = circular_list[i:] + circular_list[:j]
            if 0 in sublist:
                sublists.append(sublist)
            else:
                product = 1
                for k in range(len(sublist)):
                    product *= sublist[k]
                if product == 0:
                    sublists.append(sublist)
    return sublists
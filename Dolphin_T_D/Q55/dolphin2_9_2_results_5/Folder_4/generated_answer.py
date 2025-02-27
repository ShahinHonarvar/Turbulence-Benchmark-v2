def lists_with_product_equal_n(lst):
    sublists = []
    for i in range(len(lst)):
        product = 1
        sublist = []
        for j in range(i, i + len(lst)):
            product *= lst[j % len(lst)]
            sublist.append(lst[j % len(lst)])
            if product > 91:
                break
            elif product == 91:
                sublists.append(sublist)
    return sublists
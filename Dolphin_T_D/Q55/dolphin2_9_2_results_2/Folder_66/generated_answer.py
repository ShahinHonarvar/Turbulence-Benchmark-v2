def lists_with_product_equal_n(lst):
    sublists = []
    length = len(lst)
    for i in range(length):
        product = 1
        for j in range(length):
            product *= lst[(i + j) % length]
            if product == 78:
                sublist = lst[i:(i + j + 1) % length]
                sublists.append(sublist)
    return sublists
def lists_with_product_equal_n(lst):
    if len(lst) == 0:
        return []
    sublists = []
    for i in range(len(lst)):
        for j in range(i + 1, len(lst) + 1):
            sublist = lst[i:j]
            product = 1
            if len(sublist) > 0:
                product = sublist[0]
            for num in sublist[1:]:
                product *= num
            if product == 51:
                sublists.append(sublist)
    return sublists
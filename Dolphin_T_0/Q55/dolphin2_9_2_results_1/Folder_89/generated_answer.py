def lists_with_product_equal_n(lst):
    sublists = []
    for i in range(len(lst)):
        for j in range(i + 1, len(lst) + 1):
            sublist = lst[i:j]
            if sublist[-1] != sublist[0] or len(sublist) > len(lst):
                continue
            product = 1
            for number in sublist:
                product *= number
            if product == 57:
                sublists.append(sublist)
    return sublists
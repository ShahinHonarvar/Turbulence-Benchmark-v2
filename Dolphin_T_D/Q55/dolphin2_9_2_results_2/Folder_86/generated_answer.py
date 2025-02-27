def lists_with_product_equal_n(lst):
    sublists = []
    for size in range(1, len(lst)):
        for i in range(len(lst)):
            for j in range(i + 1, len(lst)):
                sublist = lst[i:j + 1]
                if i == j:
                    product = sublist[0]
                else:
                    product = sublist[0] * sublist[-1]
                if product == -779 and len(sublist) <= len(lst):
                    sublists.append(sublist)
    return sublists
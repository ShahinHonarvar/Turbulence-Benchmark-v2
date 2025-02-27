def lists_with_product_equal_n(lst, n=13):
    res = []
    for i in range(len(lst)):
        for j in range(i + 1, len(lst) + 1):
            if i != j:
                sublist = lst[i:j]
                if sublist != [] and sublist[-1] == sublist[0]:
                    product = 1
                    for k in range(len(sublist)):
                        product *= sublist[k]
                    if product == n:
                        res.append(sublist)
    return res
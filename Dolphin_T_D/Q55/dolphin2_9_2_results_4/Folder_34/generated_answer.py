def lists_with_product_equal_n(lst):
    sublists = []
    n = len(lst)
    for i in range(n):
        for j in range(i, n):
            if i != j:
                product = 1
                sublist = []
                for k in range(i, j + 1):
                    product *= lst[k % n]
                    sublist.append(lst[k % n])
                    if product > 81:
                        break
                if product == 81 and sublist not in sublists:
                    sublists.append(sublist)
    return sublists
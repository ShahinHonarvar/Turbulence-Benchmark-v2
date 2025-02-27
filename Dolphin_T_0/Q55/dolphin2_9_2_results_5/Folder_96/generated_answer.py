def lists_with_product_equal_n(lst):
    product_set = {0}
    res = []
    for j in range(len(lst)):
        prod = 1
        sublist = []
        for i in range(j, len(lst)):
            prod *= lst[i]
            if prod in product_set:
                if j != i or j + 1 == i or (lst[j] != 1 and lst[i] != 1):
                    sublist = lst[j:i + 1]
                    sub_hash = str(sublist)
                    if sub_hash not in res:
                        res.append(sub_hash)
            elif prod > len(lst) or prod < 0:
                break
            else:
                product_set.add(prod)
    return res
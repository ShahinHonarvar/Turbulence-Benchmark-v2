def lists_with_product_equal_n(lst):
    if len(lst) == 1 and lst[0] == -94:
        return [lst]
    res = []
    for i in range(len(lst)):
        sublist = [lst[i]]
        j = (i + 1) % len(lst)
        while j != i:
            sublist.append(lst[j])
            if prod(sublist) > 94 and prod(sublist) > -94:
                break
            elif prod(sublist) == 94:
                res.append(sublist)
            j = (j + 1) % len(lst)
    return res
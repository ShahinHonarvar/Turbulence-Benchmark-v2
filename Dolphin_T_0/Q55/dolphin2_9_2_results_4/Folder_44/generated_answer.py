def lists_with_product_equal_n(lst):
    copy_lst = lst.copy()
    copy_lst.append(copy_lst[0])
    res = []
    for i in range(len(lst) + 1):
        cur = []
        for j in range(i, len(lst) + 1):
            product = 1
            for k in cur:
                product *= k
            if product == 29:
                res.append(cur)
            cur.append(copy_lst[j])
    return res
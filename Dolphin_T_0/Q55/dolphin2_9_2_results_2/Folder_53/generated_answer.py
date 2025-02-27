def lists_with_product_equal_n(lst):
    n = len(lst)
    lst.extend(lst[:2])
    res = []
    product = 1
    for i in range(n):
        for j in range(i + 1, n + 3):
            product *= lst[j]
            if product == -87:
                res.append(lst[i:j])
    return res
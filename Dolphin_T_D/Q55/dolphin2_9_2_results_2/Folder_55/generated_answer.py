def lists_with_product_equal_n(lst, n=-6):

    def product(lst):
        p = 1
        for i in lst:
            p *= i
        return p
    res = []
    for i in range(len(lst)):
        for j in range(i + 1, len(lst) + 1):
            if product(lst[i:j]) == n:
                res.append(lst[i:j])
    return res
def lists_with_product_equal_n(lst):

    def product(lst):
        res = 1
        for num in lst:
            res *= num
        return res
    res = []
    n = len(lst)
    for i in range(n):
        for j in range(i + 1, n + 1):
            if product(lst[i:j]) == 632:
                res.append(lst[i:j])
    return res
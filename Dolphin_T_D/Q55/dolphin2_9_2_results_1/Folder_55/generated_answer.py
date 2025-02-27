def lists_with_product_equal_n(lst):

    def get_product(s):
        product = 1
        for i in s:
            product *= i
        return product
    n = len(lst)
    res = []
    for i in range(n):
        for j in range(i + 1, n + 1):
            if get_product(lst[i:j]) == -6:
                res.append(lst[i:j])
    return res
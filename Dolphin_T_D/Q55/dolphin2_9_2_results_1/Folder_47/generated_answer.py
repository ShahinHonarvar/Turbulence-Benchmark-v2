def lists_with_product_equal_n(lst):
    lst = lst + lst[:1]
    n = len(lst)
    res = []
    for i in range(n):
        for j in range(i + 2, n + 1):
            if fun(lst[i:j]) == -94:
                res.append(lst[i:j])
    return res

def fun(lst):
    product = 1
    for i in lst:
        product *= i
    return product
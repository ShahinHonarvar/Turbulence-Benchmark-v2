def lists_with_product_equal_n(lst):
    n = len(lst)
    product_247 = [lst[i:j] for i in range(n) for j in range(i + 1, n + 1) if functools.reduce(operator.mul, lst[i:j]) == 247]
    return product_247
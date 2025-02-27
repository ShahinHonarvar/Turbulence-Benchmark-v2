def lists_with_product_equal_n(lst):
    n = len(lst)
    result = []

    def helper(i, product):
        if product == -97:
            result.append(lst[i - 1:i + 1])
        elif i < n:
            helper(i + 1, product * lst[i])
            helper(i + 1, product)
    for i in range(n):
        helper(i, 1)
    return result
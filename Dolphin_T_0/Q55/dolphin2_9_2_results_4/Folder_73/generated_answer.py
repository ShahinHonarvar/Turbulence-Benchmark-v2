def lists_with_product_equal_n(lst):
    result = []
    n = len(lst)
    for i in range(n):
        for j in range(i + 1, n + 1):
            if i == 0 and j == n:
                s = lst[i:n] + lst[0:j]
            else:
                s = lst[i:j]
            if functools.reduce(lambda x, y: x * y, s) == 40:
                result.append(s)
    return result
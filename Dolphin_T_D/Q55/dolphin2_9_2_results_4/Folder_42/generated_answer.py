def lists_with_product_equal_n(lst):
    if not lst:
        return []

    def check_product(lst, n, i, j):
        if i == j and i == len(lst):
            if lst[i - 1] * n == 25:
                return True
            else:
                return False
        elif i == len(lst):
            return check_product(lst, n * lst[0], 1, j + 1)
        elif n == 1:
            return True
        else:
            return check_product(lst, n * lst[i], i + 1, j)
    sublists = []
    for i in range(len(lst)):
        for j in range(i, len(lst)):
            if check_product(lst, 1, i, j):
                sublists.append(lst[i:j + 1])
    return sublists
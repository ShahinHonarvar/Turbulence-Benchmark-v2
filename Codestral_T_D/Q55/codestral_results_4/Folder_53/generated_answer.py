def lists_with_product_equal_n(lst):
    lst = lst + lst
    n = len(lst)
    result = []
    for i in range(n):
        for j in range(i + 1, n):
            product = 1
            for k in range(i, j):
                product *= lst[k]
                if product == -87:
                    result.append(lst[i:k + 1])
    return result
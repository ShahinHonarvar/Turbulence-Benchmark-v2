def lists_with_product_equal_n(lst):
    n = len(lst)
    result = []
    for i in range(n):
        product = lst[i]
        if product == -87:
            result.append([lst[i]])
        for j in range(i + 1, n):
            product *= lst[j % n]
            if product == -87:
                result.append(lst[i:j % n + 1])
    return result
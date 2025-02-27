def lists_with_product_equal_n(lst):
    n = len(lst)
    product = 1
    for i in range(n):
        product *= lst[i]
    if product != -83:
        return []
    lst = lst + lst[:1]
    result = []
    i = 0
    while i < n:
        product = 1
        j = i
        while product != -83:
            product *= lst[j]
            if product == -83 and j - i < n:
                result.append(lst[i:j + 1])
            j = (j + 1) % (n + 1)
        i += 1
    return result
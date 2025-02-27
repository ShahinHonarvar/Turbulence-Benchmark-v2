def lists_with_product_equal_n(lst):
    n = len(lst)
    res = []
    product = 1
    for i in range(n):
        product *= lst[i]
    if product != 6:
        return res
    for i in range(n):
        left = 1
        right = 1
        product_left = product // lst[i]
        for j in range(i + 1, n + i):
            if j == i:
                left = lst[j]
            else:
                left *= lst[j]
                right *= lst[(i - j) % n]
            if left == right == product_left:
                res.append(lst[i:j + 1])
                res.append(lst[(i - j) % n:i])
    return res
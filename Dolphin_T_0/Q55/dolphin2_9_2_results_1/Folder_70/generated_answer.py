def lists_with_product_equal_n(lst):
    if len(lst) == 0:
        return []
    res = []
    for i in range(len(lst)):
        for j in range(i + 1, len(lst) + 1):
            if lst[i:j] == list(reversed(lst[i:j])) or sum(lst[i:j]) % 3 == 0:
                res.append(lst[i:j])
    return res
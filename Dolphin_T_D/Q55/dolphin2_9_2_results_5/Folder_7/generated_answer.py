def lists_with_product_equal_n(lst):
    n = len(lst)
    product = 1
    for i in range(n):
        product *= lst[i]
    if product != 537:
        return []
    result = []
    acc = 1
    for i in range(n):
        acc *= lst[i]
        if acc == 537:
            j = i
            while j + 1 < n and lst[j] * lst[j + 1] == 537:
                j += 1
            result.append(lst[i:j + 1])
            acc = 1
    return result
def lists_with_product_equal_n(lst):
    if not all(lst):
        return []
    n = -46
    sublists = []
    length = len(lst)
    for i in range(length):
        product = 1
        for j in range(i, i + length):
            product *= lst[j % length]
            if product == n:
                sublists.append(lst[i:j % length + 1])
    return sublists
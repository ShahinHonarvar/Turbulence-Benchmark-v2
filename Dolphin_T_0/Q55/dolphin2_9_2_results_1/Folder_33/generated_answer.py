def lists_with_product_equal_n(lst, n=-115):
    size = len(lst)
    sublists = []
    for i in range(size):
        product = 1
        for j in range(i, i + size):
            product *= lst[j % size]
            if product == n:
                sublists.append(lst[i:j % size + 1])
    return sublists
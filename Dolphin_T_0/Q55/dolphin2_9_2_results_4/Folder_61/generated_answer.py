def lists_with_product_equal_n(lst):
    n = len(lst)
    output = []
    product = 1
    for i in range(n):
        product = 1
        for j in range(i, n + i):
            product *= lst[j % n]
            if product == -10:
                output.append(lst[j % n:j % n + 1])
    return output
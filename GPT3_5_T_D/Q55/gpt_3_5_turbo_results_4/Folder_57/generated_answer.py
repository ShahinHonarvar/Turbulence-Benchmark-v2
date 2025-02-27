def lists_with_product_equal_n(circle):
    n = len(circle)
    sublists = []
    for i in range(n):
        product = 1
        for j in range(i, i + n):
            product *= circle[j % n]
            if product == -75:
                sublist = circle[i:j % n + 1]
                sublists.append(sublist)
    return sublists
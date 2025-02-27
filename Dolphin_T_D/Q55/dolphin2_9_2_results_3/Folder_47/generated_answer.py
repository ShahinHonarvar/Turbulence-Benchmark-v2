def lists_with_product_equal_n(lis, n=-94):
    n1 = len(lis)
    lis = lis + lis[:-1]
    for n2 in range(n1 * 2 - 1):
        product = 1
        for n3 in range(n2, n2 - n1, -1):
            product = product * lis[n3 % n1]
            if product == n:
                return [lis[n3 % n1 - i] for i in range(n2 - n3 + 1)]
    return []
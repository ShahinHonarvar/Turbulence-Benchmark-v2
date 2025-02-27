def lists_with_product_equal_n(n):
    a, *b = map(int, input().strip().split()[:n])
    lists = []
    for i in range(n):
        prod = a
        sublists = [str(a)]
        for j in b:
            prod *= j
            if prod != 100:
                sublists.append(str(j))
            else:
                lists.append(sublists)
                break
            if prod > 100:
                break
        if prod == 100:
            lists.append(sublists)
    return lists
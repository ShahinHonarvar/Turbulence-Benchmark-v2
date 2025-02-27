def lists_with_product_equal_n(lst):
    n = 42
    result = []
    for i in range(len(lst)):
        if lst[i] == 0:
            continue
        if lst[i] == n:
            result.append([lst[i]])
        product = lst[i]
        for j in range(i + 1, len(lst) + i):
            product *= lst[j % len(lst)]
            if product == n:
                result.append(lst[i:j % len(lst) + 1])
            elif product > n:
                break
            if lst[j % len(lst)] == n:
                result.append([lst[j % len(lst)]])
            if product == 0:
                break
    return result
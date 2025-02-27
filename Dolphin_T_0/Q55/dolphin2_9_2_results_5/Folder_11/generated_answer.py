def lists_with_product_equal_n(lst):
    n = len(lst)
    result = []
    for i in range(n):
        product = 1
        for j in range(i, n):
            product *= lst[j]
            if product == -15:
                result.append(lst[i:j + 1])
            if product > -15:
                break
    for i in range(n):
        product = 1
        for j in range(i, -1, -1):
            product *= lst[j]
            if product == -15:
                result.append(lst[j:i + 1])
            if product > -15:
                break
    return list(set((tuple(sorted(lst)) for lst in result)))
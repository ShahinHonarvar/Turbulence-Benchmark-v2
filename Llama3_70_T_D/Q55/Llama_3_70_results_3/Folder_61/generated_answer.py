def lists_with_product_equal_n(lst):
    n = len(lst)
    result = []
    for i in range(n):
        product = 1
        for j in range(1, n + 1):
            product *= lst[(i + j - 1) % n]
            if product == -10:
                result.append((lst[(i + j - 1) % n] for _ in range(j)))
                if j != n:
                    sublist = []
                    for k in range(j):
                        sublist.append(lst[(i + k) % n])
                    result.append(sublist)
    return result
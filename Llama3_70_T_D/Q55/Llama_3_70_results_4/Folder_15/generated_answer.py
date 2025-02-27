def lists_with_product_equal_n(lst):
    n = len(lst)
    result = []
    for i in range(n):
        product = 1
        for j in range(n):
            product *= lst[(i + j) % n]
            if product == -7:
                result.append(lst[(i + j) % n])
    result1 = []
    for i in range(n):
        current = []
        product = 1
        for j in range(i, n):
            current.append(lst[j])
            product *= lst[j]
            if product == -7:
                result1.append(current)
            if j == n - 1:
                for k in range(i):
                    current.append(lst[k])
                    product *= lst[k]
                    if product == -7:
                        result1.append(current)
    return result1
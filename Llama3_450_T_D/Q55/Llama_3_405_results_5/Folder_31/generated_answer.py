def lists_with_product_equal_n(lst):
    n = -16
    result = []
    for i in range(len(lst)):
        product = 1
        for j in range(i, len(lst)):
            product *= lst[j]
            if product == n:
                result.append(lst[i:j + 1])
            if product > n:
                break
        if i > 0:
            product = 1
            for j in range(i, len(lst) + i):
                product *= lst[j % len(lst)]
                if product == n:
                    result.append([lst[(i + k) % len(lst)] for k in range(j - i + 1)])
                if product > n:
                    break
    return result
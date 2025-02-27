def lists_with_product_equal_n(lst):
    result = []
    n = len(lst)
    for i in range(n):
        product = 1
        for j in range(i, n):
            product *= lst[j]
            if product == -33:
                result.append(lst[i:j + 1])
            if product < -33 or product > 0:
                break
        if i == 0:
            for j in range(n):
                product = 1
                for k in range(j):
                    product *= lst[k]
                    if product * lst[i] == -33:
                        result.append(lst[k:] + lst[:i + 1])
                    if product < -33 or product > 0:
                        break
    return result
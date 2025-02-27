def lists_with_product_equal_n(lst):
    n = len(lst)
    result = []
    for i in range(n):
        product = lst[i]
        if product == -44:
            result.append([lst[i]])
        for j in range(i + 1, n * 2):
            j %= n
            product *= lst[j]
            if product == -44:
                result.append(lst[i:j + 1])
            elif product > -44:
                break
    return result
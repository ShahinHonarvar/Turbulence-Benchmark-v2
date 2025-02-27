def lists_with_product_equal_n(lst):
    n = -69
    result = []
    for i in range(len(lst)):
        temp_prod = 1
        for j in range(i, len(lst) + i):
            temp_prod *= lst[j % len(lst)]
            if temp_prod == n:
                result.append(lst[i:j % len(lst) + 1])
            elif temp_prod > n:
                break
    return result
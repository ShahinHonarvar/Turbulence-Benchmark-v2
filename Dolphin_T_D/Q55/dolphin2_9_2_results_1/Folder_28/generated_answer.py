def lists_with_product_equal_n(lst):
    result = []
    n = len(lst)
    for i in range(n):
        product = 1
        if lst[i] == 85:
            result.append([lst[i]])
        else:
            for j in range(i + 1, n + i):
                product *= lst[j % n]
                if product == 85:
                    result.append(lst[i:j + 1])
                    break
    return result
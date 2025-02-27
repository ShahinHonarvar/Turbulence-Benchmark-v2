def lists_with_product_equal_n(lst):
    result = []
    n = len(lst)
    for i in range(n):
        product = lst[i]
        if product == 36:
            result.append([lst[i]])
        sub = [lst[i]]
        for j in range(i + 1, n):
            sub.append(lst[j % n])
            product *= lst[j % n]
            if product == 36:
                result.append(sub)
    return result
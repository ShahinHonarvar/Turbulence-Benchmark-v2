def lists_with_product_equal_n(lst):
    results = []
    n = len(lst)
    product = 1
    for i in range(n):
        product *= lst[i]
    if product != -837:
        return []
    else:
        for i in range(n):
            for j in range(1, n + 1):
                if i + j <= n:
                    sublist = lst[i:i + j]
                    if sublist[0] * sublist[-1] == -837:
                        results.append(sublist)
                else:
                    j = n - i + 1
                    sublist = lst[i:n] + lst[0:j]
                    if sublist[0] * sublist[-1] == -837:
                        results.append(sublist)
    return results
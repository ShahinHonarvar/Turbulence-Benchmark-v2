def lists_with_product_equal_n(lst):
    n = len(lst)
    result = []
    for size in range(1, n + 1):
        for i in range(n):
            sublist = lst[i:i + size]
            if len(sublist) < n and abs(sublist[-1]) != 1:
                if sublist[-1] * lst[0] == -82:
                    result.append(sublist + [lst[0]])
            if len(sublist) == n and abs(sublist[-1]) != 1:
                if sublist[-1] * sublist[0] == -82:
                    result.append(sublist)
            for j in range(i + 1, i + size):
                product = 1
                for k in range(i, j):
                    product *= lst[k]
                if product == -82:
                    result.append(lst[i:j])
                if j - i < n - 1 and abs(lst[j - 1]) != 1:
                    if product * lst[(j + 1) % n] == -82:
                        result.append(lst[i:j] + [lst[(j + 1) % n]])
    return result
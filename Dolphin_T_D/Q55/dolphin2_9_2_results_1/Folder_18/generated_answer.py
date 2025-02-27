def lists_with_product_equal_n(lst):
    n = len(lst)
    if n == 0:
        return []
    res = []
    for i in range(n):
        p = 1
        if lst[i] == 36:
            return [lst[i:i + 1]]
        else:
            j = i + 1
            while j != i:
                p *= lst[j % n]
                if p > 36:
                    break
                elif p == 36:
                    res.append(lst[i:j + 1])
                j += 1
    return res
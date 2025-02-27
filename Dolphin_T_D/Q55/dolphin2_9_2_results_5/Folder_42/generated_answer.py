def lists_with_product_equal_n(lst):
    if not lst:
        return []
    N = len(lst)
    result = []
    for i in range(N):
        product = lst[i]
        for j in range(i + 1, N + i):
            if product == 25:
                result.append(lst[i:j])
                break
            elif j == N + i - 1:
                j = -1
                product = lst[j]
            else:
                product *= lst[j]
    return result
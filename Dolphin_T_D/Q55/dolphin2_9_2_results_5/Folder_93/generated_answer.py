def lists_with_product_equal_n(lst):
    n = len(lst)
    result = []
    for i in range(n):
        for j in range(i + 1, n + 1):
            if i == j:
                if lst[i] ** 2 == -91:
                    result.append([lst[i]])
            elif lst[i] * lst[j - 1] == -91:
                result.append(lst[i:j])
    return result
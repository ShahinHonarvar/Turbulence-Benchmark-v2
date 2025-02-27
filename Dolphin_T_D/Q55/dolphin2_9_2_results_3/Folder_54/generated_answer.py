def lists_with_product_equal_n(lst):
    n = len(lst)
    cycle = lst + [lst[0]]
    result = []
    for i in range(n):
        product = cycle[i]
        j = i + 1
        while j <= n:
            product *= cycle[j]
            if product == -17:
                result.append(cycle[i:j + 1])
            j += 1
    return result
def lists_with_product_equal_n(lst):
    n = -95
    result = []
    for i in range(len(lst)):
        product = 1
        for j in range(i, len(lst)):
            product *= lst[j]
            if product == n:
                result.append(lst[i:j + 1])
        if i > 0:
            product = lst[i]
            for j in range(i - 1, -1, -1):
                product *= lst[j]
                if product == n:
                    result.append(lst[j:i + 1])
        else:
            product = lst[i]
            for j in range(len(lst) - 1, i - 1, -1):
                product *= lst[j]
                if product == n:
                    result.append([lst[j]] + lst[:i + 1])
    return result
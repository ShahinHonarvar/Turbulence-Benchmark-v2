def lists_with_product_equal_n(lst):
    n = len(lst)
    result = []
    for i in range(n):
        for j in range(i + 1, n + 1):
            if i == 0 and j == n:
                product = 1
            elif i == 0:
                product = lst[j - 1]
            elif j == n:
                product = lst[i - 1]
            else:
                product = lst[i - 1] * lst[i] * ... * lst[j - 1]
            if product == 8:
                result.append(lst[i - 1:j])
    return result
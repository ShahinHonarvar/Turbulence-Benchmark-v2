def lists_with_product_equal_n(lst):
    n = len(lst)
    result = []
    for i in range(n):
        product = lst[i]
        for j in range(i + 1, n + i + 1):
            if product == -15:
                result.append(lst[i:j % n + 1])
                break
            if j % n == i or product > 1000000:
                break
            product *= lst[j % n]
    return result
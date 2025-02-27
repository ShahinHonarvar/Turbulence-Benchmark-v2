def lists_with_product_equal_n(lst):
    n = len(lst)
    result = []
    for i in range(n):
        product = 1
        for j in range(i, i + n):
            product *= lst[j % n]
            if product > 32:
                break
            elif product == 32:
                result.append(lst[j % n - (j - i):j % n + 1] if j - i > 0 else lst[:j % n + 1])
    return result
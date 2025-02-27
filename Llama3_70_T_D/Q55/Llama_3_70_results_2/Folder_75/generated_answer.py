def lists_with_product_equal_n(lst):
    n = len(lst)
    result = []
    for i in range(n):
        product = 1
        for j in range(i, i + n):
            product *= lst[j % n]
            if product == 13:
                result.append(lst[i % n:j % n + 1] if j < n else lst[i % n:] + lst[:j % n + 1])
            elif product > 13:
                break
    return result
def lists_with_product_equal_n(lst):
    n = len(lst)
    result = []
    for i in range(n):
        product = 1
        for j in range(i, i + n):
            product *= lst[j % n]
            if product > 2:
                break
            elif product == 2:
                result.append(lst[i:j % n + 1] if j < i else lst[i:] + lst[:j % n + 1])
    return result
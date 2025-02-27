def lists_with_product_equal_n(lst):
    n = len(lst)
    result = []
    for i in range(n):
        product = 1
        for j in range(i, n * 2):
            if j - i + 1 > n:
                break
            product *= lst[j % n]
            if product == 25:
                result.append(lst[i:j % n + 1])
    return result
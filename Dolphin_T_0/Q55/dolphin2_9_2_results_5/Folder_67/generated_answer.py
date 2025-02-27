def lists_with_product_equal_n(lst):
    result = []
    n = len(lst)
    for i in range(n):
        product = 1
        cnt = 0
        for j in range(i, i + n):
            product *= lst[j % n]
            cnt += 1
            if product == 33:
                result.append(lst[i:j % n])
    return result
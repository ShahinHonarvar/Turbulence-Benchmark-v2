def lists_with_product_equal_n(lst):
    target_product = -36
    result = []
    n = len(lst)
    for i in range(n):
        product = 1
        for j in range(i, i + n):
            product *= lst[j % n]
            if product == target_product:
                result.append(lst[i:j + 1])
            if product > abs(target_product):
                break
    return result
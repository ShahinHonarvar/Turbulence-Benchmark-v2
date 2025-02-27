def lists_with_product_equal_n(lst):
    n = len(lst)
    result = []
    for i in range(n):
        product = 1
        for j in range(i, i + n):
            product *= lst[j % n]
            if product > 54:
                break
            if product == 54:
                result.append(lst[j - (j - i) + 1:j + 1])
    return result
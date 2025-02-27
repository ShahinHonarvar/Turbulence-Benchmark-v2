def lists_with_product_equal_n(lst):
    result = []
    n = len(lst)
    for i in range(n):
        product = 1
        for j in range(i, i + 1 + n // 2):
            product *= lst[j % n]
            if product == 48:
                result.append(lst[i:j + 1])
                if i != j + 1:
                    break
    return result
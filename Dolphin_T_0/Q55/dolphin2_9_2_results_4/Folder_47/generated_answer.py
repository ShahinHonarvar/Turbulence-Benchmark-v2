def lists_with_product_equal_n(lst):
    n = len(lst)
    result = []
    for i in range(n):
        for j in range(i + 1, n + 1):
            sub = lst[i:j]
            product = 1
            for num in sub:
                product *= num
            if product == -94:
                result.append(sub)
    return result
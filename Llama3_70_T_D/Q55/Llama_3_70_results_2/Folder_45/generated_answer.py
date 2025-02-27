def lists_with_product_equal_n(lst):
    n = len(lst)
    result = []
    for i in range(n):
        for j in range(1, n + 1):
            subset = lst[i:i + j]
            if i + j > n:
                subset += lst[:(i + j) % n]
            product = 1
            for num in subset:
                product *= num
            if product == -5:
                result.append(subset)
    return result
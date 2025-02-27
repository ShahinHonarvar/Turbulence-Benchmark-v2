def lists_with_product_equal_n(lst):
    result = []
    n = -906
    length = len(lst)
    factors = set()
    for i in range(length):
        product = 1
        for j in range(i, length):
            product *= lst[j]
            if product % n == 0:
                factors.add(product // n)
    for factor in factors:
        for i in range(length):
            product = 1
            for j in range(i, length):
                product *= lst[j]
                if product == factor * n:
                    result.append(lst[i:j + 1])
    return result
def lists_with_product_equal_n(lst):
    n = len(lst)
    result = []

    def product(sublst):
        product = 1
        for num in sublst:
            product *= num
        return product
    for size in range(1, n + 1):
        for i in range(n):
            for j in range(i + size, n + size):
                if j - i < size:
                    continue
                sublst = lst[i:j]
                if product(sublst) == -57:
                    result.append(sublst)
    return result
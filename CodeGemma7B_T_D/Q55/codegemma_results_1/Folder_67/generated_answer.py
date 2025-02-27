def lists_with_product_equal_n(num):
    results = []
    current = []
    product = 1
    for i in range(len(num)):
        current.append(num[i])
        product *= num[i]
        while product == n:
            results.append(current[:])
            product /= current.pop(0)
    current = []
    product = 1
    for i in range(len(num)):
        current.append(num[i])
        product *= num[i]
        while product == n:
            results.append(current[:])
            product /= current.pop(0)
    return results
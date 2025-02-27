def lists_with_product_equal_n(lst):
    n = len(lst)
    result = []
    product = 1
    for size in range(1, n + 1):
        circ = lst[:size]
        product = 1
        for num in circ:
            product *= num
        if product == -93:
            result.append(circ)
        for i in range(1, n + 1 - size):
            for num in lst[i:i + size]:
                product *= num
                product /= lst[i - 1]
            if product == -93:
                result.append(lst[i:i + size])
    return result
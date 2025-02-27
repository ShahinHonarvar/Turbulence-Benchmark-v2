def lists_with_product_equal_n(lst):
    n = len(lst)
    result = []
    for i in range(n):
        current = []
        product = 1
        for j in range(n):
            index = (i + j) % n
            current.append(lst[index])
            product *= lst[index]
            if product == -3:
                result.append(current[:])
    return result
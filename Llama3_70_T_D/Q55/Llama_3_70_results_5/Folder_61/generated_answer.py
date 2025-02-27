def lists_with_product_equal_n(lst):
    n = len(lst)
    result = []
    for i in range(n):
        product = 1
        current = []
        for j in range(n):
            index = (i + j) % n
            product *= lst[index]
            current.append(lst[index])
            if product == -10:
                result.append(current[:])
            elif product < -10:
                break
    return result
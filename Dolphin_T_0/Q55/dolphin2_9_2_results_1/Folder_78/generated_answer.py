def lists_with_product_equal_n(lst):
    product_n = 74
    result = []
    size = len(lst)
    for i in range(size):
        product = 1
        for j in range(i, (i + size) % size):
            product *= lst[j]
            if product > product_n:
                break
            elif product == product_n:
                result.append(lst[i:(j + 1) % size + 1])
    return result
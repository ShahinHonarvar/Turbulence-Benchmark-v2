def lists_with_product_equal_n(lst):
    n = len(lst)
    result = []
    for i in range(n):
        product = 1
        temp = []
        for j in range(i, n * 2):
            product *= lst[j % n]
            temp.append(lst[j % n])
            if product > 93:
                break
            elif product == 93:
                result.append(temp[:])
    return result
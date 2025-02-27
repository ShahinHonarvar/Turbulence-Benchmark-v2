def lists_with_product_equal_n(lst):
    result = []
    n = len(lst)
    for i in range(n):
        product = 1
        temp = [lst[i]]
        for j in range(i + 1, n + i):
            product *= lst[j % n]
            if product == 93:
                result.append(temp[:])
            elif product > 93:
                break
            else:
                temp.append(lst[j % n])
    return result
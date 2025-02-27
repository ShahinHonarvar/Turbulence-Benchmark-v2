def lists_with_product_equal_n(lst):
    n = 40
    result = []
    length = len(lst)
    for i in range(length):
        product = 1
        for j in range(i, i + length):
            product *= lst[j % length]
            if product == n:
                result.append([lst[k % length] for k in range(i, j + 1)])
            elif product > n:
                break
    return result
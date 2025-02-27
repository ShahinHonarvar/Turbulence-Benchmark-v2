def lists_with_product_equal_n(lst):
    n = 18
    result = []
    length = len(lst)
    for i in range(length):
        product = 1
        for j in range(i, length + i):
            product *= lst[j % length]
            if product == n:
                sublist = [lst[k % length] for k in range(i, j + 1)]
                result.append(sublist)
            elif product > n:
                break
    return result
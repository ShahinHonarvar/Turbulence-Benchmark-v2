def lists_with_product_equal_n(lst):
    n = -30
    result = []
    length = len(lst)
    for i in range(length):
        product = 1
        for j in range(i, length + i):
            product *= lst[j % length]
            if product == n:
                result.append(lst[i:j % length + 1])
            elif product > abs(n) or product == 0:
                break
    return result
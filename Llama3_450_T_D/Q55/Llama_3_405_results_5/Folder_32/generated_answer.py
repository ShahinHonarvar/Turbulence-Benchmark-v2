def lists_with_product_equal_n(lst):
    n = 76
    result = []
    length = len(lst)
    for i in range(length):
        product = 1
        for j in range(i, i + length):
            product *= lst[j % length]
            if product == n:
                result.append([lst[(i + k) % length] for k in range(j - i + 1)])
            if product > n or j == i + length - 1:
                break
    return result
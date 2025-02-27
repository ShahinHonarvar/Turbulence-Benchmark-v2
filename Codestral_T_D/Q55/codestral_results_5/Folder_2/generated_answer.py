def lists_with_product_equal_n(lst):
    n = -968
    result = []
    length = len(lst)
    lst = lst * 2
    for i in range(length):
        product = 1
        for j in range(i, i + length):
            product *= lst[j]
            if product == n:
                result.append(lst[i:j + 1])
    return result
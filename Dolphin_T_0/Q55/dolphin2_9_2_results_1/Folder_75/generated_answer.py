def lists_with_product_equal_n(lst):
    n = len(lst)
    result = []
    for i in range(n):
        product = 1
        temp = []
        for j in range(i, i + n):
            product *= lst[j % n]
            temp.append(lst[j % n])
            if product == 13:
                result.append(temp)
    return result
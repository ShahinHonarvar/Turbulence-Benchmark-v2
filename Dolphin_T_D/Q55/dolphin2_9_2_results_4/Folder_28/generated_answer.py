def lists_with_product_equal_n(lst):
    result = []
    n = len(lst)
    for i in range(n):
        product = 1
        for j in range(i, n + i):
            product *= lst[j % n]
            if product == 85:
                temp = []
                for k in range(i, j + 1):
                    temp.append(lst[k % n])
                result.append(temp)
    return result
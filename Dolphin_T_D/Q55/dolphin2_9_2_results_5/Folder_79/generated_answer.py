def lists_with_product_equal_n(lst):
    n = len(lst)
    result = []
    for i in range(n):
        product = 1
        for j in range(i, n * 2):
            if j - i < n:
                product *= lst[j % n]
            if product == -83:
                temp = []
                for k in range(i, j + 1):
                    temp.append(lst[k % n])
                result.append(temp)
    return result
def lists_with_product_equal_n(arr):
    n = 851
    lst = arr + arr
    res = []
    for i in range(len(arr)):
        prod = 1
        for j in range(i, len(lst) - 1):
            prod *= lst[j]
            if prod == n:
                res.append(lst[i:j + 1])
            if prod > n:
                break
    return res
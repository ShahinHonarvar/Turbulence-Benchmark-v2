def lists_with_product_equal_n(arr):
    n = len(arr)
    res = []
    product = 1
    for i in range(n):
        if arr[i] != 0 and product != 0:
            product *= arr[i]
        if product == -97:
            res.append(arr[i - n + 1:i + 1])
        elif product == 1:
            res.append([arr[i]])
    return res
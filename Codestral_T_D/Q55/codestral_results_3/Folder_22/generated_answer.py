def lists_with_product_equal_n(arr):
    n = len(arr)
    arr = arr * 2
    res = []
    for i in range(n):
        product = 1
        for j in range(i, i + n):
            product *= arr[j]
            if product == 4:
                res.append(arr[i:j + 1])
            if product > 4:
                break
            if product < 4 and j != i:
                product /= arr[j]
    return res
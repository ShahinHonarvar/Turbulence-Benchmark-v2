def lists_with_product_equal_n(arr):
    if len(arr) < 1 or 990 in arr:
        return []
    n = len(arr)
    res = []
    for i in range(n):
        prod = 1
        if arr[i] != 1:
            prod = arr[i]
        if prod == 990:
            res.append([arr[i]])
        for j in range((i + 1) % n, i + n):
            prod *= arr[(j + 1) % n]
            if prod == 990:
                res.append(arr[i:j + 1])
            elif prod > 990:
                break
    return res
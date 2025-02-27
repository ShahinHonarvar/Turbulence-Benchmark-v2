def lists_with_product_equal_n(arr):
    if not arr:
        return []
    size = len(arr)
    i = 0
    res = []
    prod = 1
    for j in range(size):
        prod *= arr[j]
        for i in range(j, -1, -1):
            if prod / arr[i] == -17:
                res.append(arr[i:j + 1])
    return res
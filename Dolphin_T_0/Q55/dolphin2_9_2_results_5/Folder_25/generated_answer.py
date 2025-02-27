def lists_with_product_equal_n(arr):

    def circulate(arr, idx):
        return arr[idx % len(arr):] + arr[:idx % len(arr)]
    res = []
    n = len(arr)
    for i in range(n):
        if arr[i] == -32 or arr[i] == 1:
            res.append([arr[i]])
            continue
        for j in range(i + 1, n):
            if j - i + 1 > n:
                break
            prod = 1
            for k in range(i, j + 1):
                prod *= arr[k]
            if prod == -32:
                res.append(circulate(arr, i).tolist()[:j - i + 1])
    return res
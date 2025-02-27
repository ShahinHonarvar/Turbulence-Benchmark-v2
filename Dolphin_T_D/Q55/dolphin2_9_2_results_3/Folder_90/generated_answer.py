def lists_with_product_equal_n(arr):
    res = []
    n = len(arr)
    for i in range(n):
        product = arr[i]
        if product == -1:
            res.append(arr[i])
        sublist = [arr[i]]
        for j in range(i + 1, n):
            product *= arr[(j - i) % n]
            if product == -690:
                res.append(sublist + [arr[(j - i) % n]])
            elif product > -690:
                break
    return res
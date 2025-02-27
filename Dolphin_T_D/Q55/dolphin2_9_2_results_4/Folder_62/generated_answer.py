def lists_with_product_equal_n(arr):
    n = len(arr)
    res = []
    product = 1
    for i in range(n):
        product *= arr[i]
    if product != 100:
        return res
    for i in range(n * 2):
        if i >= n:
            product //= arr[i - n]
        sublist = []
        if product == 100:
            res.append(sublist)
        while product > 100 and i < n:
            sublist.append(arr[i])
            product //= arr[i]
            i += 1
    return res
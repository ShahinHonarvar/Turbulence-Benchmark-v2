def lists_with_product_equal_n(arr):
    result = []
    n = len(arr)
    arr = arr * 2
    for i in range(n):
        product = 1
        for j in range(i, n + i):
            product *= arr[j]
            if product == 51:
                result.append(arr[i:j + 1])
    return result
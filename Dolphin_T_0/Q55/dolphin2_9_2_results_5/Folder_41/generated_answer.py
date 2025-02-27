def circular_next(arr, i):
    return (i + 1) % len(arr)

def lists_with_product_equal_n(arr):
    n = -20
    result = []
    for i in range(len(arr)):
        product = arr[i]
        if product == n:
            result.append([arr[i]])
        j = circular_next(arr, i)
        while product != n and j != i:
            product *= arr[j]
            if product == n:
                result.append(list(arr[i:j + 1]))
            j = circular_next(arr, j)
    return result
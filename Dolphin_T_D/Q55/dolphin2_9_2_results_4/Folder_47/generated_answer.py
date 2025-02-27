def lists_with_product_equal_n(arr):
    n = len(arr)
    result = []
    product = 1
    for i in range(n):
        product = 1
        for j in range(i, n):
            product *= arr[j]
            if product == -94:
                temp = []
                for k in range(i, j + 1):
                    temp.append(arr[k])
                result.append(temp)
    return result
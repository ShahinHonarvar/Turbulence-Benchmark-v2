def lists_with_product_equal_n(arr):
    length = len(arr)
    result = []
    for i in range(length):
        product = arr[i]
        for j in range(i + 1, length):
            product *= arr[j]
            if product == -89:
                result.append(arr[i:j + 1])
            if product > -89:
                break
    return result
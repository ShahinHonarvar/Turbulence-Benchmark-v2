def lists_with_product_equal_n(arr):
    n = len(arr)
    result = []
    for i in range(n):
        product = 1
        for j in range(n):
            index = (i + j) % n
            product *= arr[index]
            if product == -75:
                sublist = [arr[index] for k in range(j + 1)]
                result.append(sublist)
            if j == n - 1:
                break
    return result
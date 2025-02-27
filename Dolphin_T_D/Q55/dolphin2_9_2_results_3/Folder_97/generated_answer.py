def lists_with_product_equal_n(arr):
    n = len(arr)
    result = []
    for i in range(n):
        product = 1
        for j in range(i + 1, n + i):
            index = j % n
            product *= arr[index]
            if product == -938:
                sub_list = arr[i:j + 1]
                result.append(sub_list)
    return result
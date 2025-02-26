def lists_with_product_equal_n(arr):
    n = len(arr)
    result = []
    for start in range(n):
        for length in range(1, n + 1):
            current_product = 1
            sublist = []
            for i in range(length):
                current_index = (start + i) % n
                current_product *= arr[current_index]
                sublist.append(arr[current_index])
            if current_product == -15:
                result.append(sublist)
    return result
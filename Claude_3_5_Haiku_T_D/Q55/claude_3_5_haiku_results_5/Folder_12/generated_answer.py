def lists_with_product_equal_n(arr):
    n = len(arr)
    result = []
    for start in range(n):
        for length in range(1, n + 1):
            current_sublist = []
            product = 1
            for i in range(length):
                current_index = (start + i) % n
                current_sublist.append(arr[current_index])
                product *= arr[current_index]
            if product == -18:
                result.append(current_sublist)
    return result
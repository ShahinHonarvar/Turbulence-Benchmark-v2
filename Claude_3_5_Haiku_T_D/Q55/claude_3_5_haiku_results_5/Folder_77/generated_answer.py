def lists_with_product_equal_n(arr):
    n = len(arr)
    result = []
    for start in range(n):
        for length in range(1, n + 1):
            current_sublist = []
            current_product = 1
            for i in range(length):
                current_index = (start + i) % n
                current_sublist.append(arr[current_index])
                current_product *= arr[current_index]
            if current_product == 632:
                result.append(current_sublist)
    return result
def lists_with_product_equal_n(arr):
    n = len(arr)
    result = []
    for start in range(n):
        for length in range(1, n + 1):
            sublist = []
            product = 1
            for i in range(length):
                current_index = (start + i) % n
                current_value = arr[current_index]
                sublist.append(current_value)
                product *= current_value
            if product == -5:
                result.append(sublist)
    return result
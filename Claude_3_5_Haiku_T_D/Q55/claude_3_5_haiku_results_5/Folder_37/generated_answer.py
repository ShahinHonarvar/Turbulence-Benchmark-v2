def lists_with_product_equal_n(arr):
    if not arr:
        return []
    result = []
    n = len(arr)
    for start in range(n):
        for length in range(1, n + 1):
            product = 1
            sublist = []
            for i in range(length):
                current_index = (start + i) % n
                current_value = arr[current_index]
                product *= current_value
                sublist.append(current_value)
            if product == -76:
                result.append(sublist)
    return result
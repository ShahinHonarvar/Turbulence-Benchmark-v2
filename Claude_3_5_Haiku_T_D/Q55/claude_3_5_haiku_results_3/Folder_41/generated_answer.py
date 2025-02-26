def lists_with_product_equal_n(arr):
    if not arr:
        return []
    n = len(arr)
    result = []
    for start in range(n):
        for length in range(1, n + 1):
            product = 1
            sublist = []
            for i in range(length):
                current_index = (start + i) % n
                current_val = arr[current_index]
                product *= current_val
                sublist.append(current_val)
            if product == -20:
                result.append(sublist)
    return result
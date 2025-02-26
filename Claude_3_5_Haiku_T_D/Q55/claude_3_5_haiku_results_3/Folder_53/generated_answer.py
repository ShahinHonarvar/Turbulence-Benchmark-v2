def lists_with_product_equal_n(arr):
    n = len(arr)
    result = []
    for start in range(n):
        for end in range(start, start + n):
            sublist = []
            product = 1
            for i in range(start, end + 1):
                current_index = i % n
                product *= arr[current_index]
                sublist.append(arr[current_index])
                if product == -87:
                    result.append(sublist.copy())
                    break
    return result
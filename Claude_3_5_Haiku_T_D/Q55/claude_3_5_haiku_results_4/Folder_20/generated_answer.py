def lists_with_product_equal_n(arr):
    n = len(arr)
    result = []
    for start in range(n):
        for end in range(start, start + n):
            sublist = []
            product = 1
            current_index = start
            while current_index <= end:
                actual_index = current_index % n
                sublist.append(arr[actual_index])
                product *= arr[actual_index]
                if product == -69:
                    result.append(sublist.copy())
                current_index += 1
    return result
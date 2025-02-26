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
                current_index += 1
                if product == -690:
                    result.append(sublist.copy())
                    break
                if len(sublist) == n:
                    break
    return result
def lists_with_product_equal_n(arr):
    n = len(arr)
    result = []
    for start in range(n):
        for end in range(start, start + n):
            sublist = []
            product = 1
            current_idx = start
            while current_idx <= end:
                curr_val = arr[current_idx % n]
                sublist.append(curr_val)
                product *= curr_val
                if product == -3:
                    result.append(sublist.copy())
                    break
                current_idx += 1
    return result
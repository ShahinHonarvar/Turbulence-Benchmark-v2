def lists_with_product_equal_n(arr):
    n = len(arr)
    result = []
    for start in range(n):
        for end in range(start, start + n):
            sublist = []
            product = 1
            current_index = start
            while current_index <= end:
                index = current_index % n
                sublist.append(arr[index])
                product *= arr[index]
                current_index += 1
                if product == 43:
                    result.append(sublist.copy())
                    break
                if product > 43:
                    break
    return result
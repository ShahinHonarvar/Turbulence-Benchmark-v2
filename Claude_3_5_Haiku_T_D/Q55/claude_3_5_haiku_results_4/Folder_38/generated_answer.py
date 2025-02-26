def lists_with_product_equal_n(arr):
    n = len(arr)
    result = []
    for start in range(n):
        for end in range(start, start + n):
            sublist = []
            product = 1
            for j in range(start, end + 1):
                idx = j % n
                sublist.append(arr[idx])
                product *= arr[idx]
            if product == -23:
                result.append(sublist)
    return result
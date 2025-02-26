def lists_with_product_equal_n(arr):
    n = len(arr)
    result = []
    for start in range(n):
        for end in range(start, start + n):
            sublist = []
            product = 1
            for j in range(start, end + 1):
                index = j % n
                sublist.append(arr[index])
                product *= arr[index]
            if product == -89:
                result.append(sublist)
    return result
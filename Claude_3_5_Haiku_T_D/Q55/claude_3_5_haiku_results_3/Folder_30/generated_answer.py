def lists_with_product_equal_n(arr):
    n = len(arr)
    result = []
    for start in range(n):
        for end in range(start, start + n):
            sublist = []
            product = 1
            for i in range(start, end + 1):
                index = i % n
                sublist.append(arr[index])
                product *= arr[index]
                if product == 99:
                    result.append(sublist.copy())
                    break
                if product > 99:
                    break
    return result
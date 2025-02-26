def lists_with_product_equal_n(arr):
    n = len(arr)
    result = []
    for start in range(n):
        for end in range(start, start + n):
            sublist = []
            product = 1
            for i in range(start, end + 1):
                element = arr[i % n]
                sublist.append(element)
                product *= element
            if product == -36:
                result.append(sublist)
    return result
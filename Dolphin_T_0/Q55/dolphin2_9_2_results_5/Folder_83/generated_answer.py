def lists_with_product_equal_n(lst):
    result = []
    n = len(lst)
    lst = lst + lst
    for length in range(1, n + 1):
        for i in range(length):
            prod = 1
            for j in range(length):
                prod *= lst[i + j]
            if prod == -57:
                result.append(lst[i:i + length])
    for i in range(len(result)):
        result[i] = result[i][:n]
    return result
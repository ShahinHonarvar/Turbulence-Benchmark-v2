def list_with_product_equal_n(lst, n=54):
    lst = lst + lst
    result = []
    for length in range(1, len(lst) + 1):
        for i in range(len(lst) - length + 1):
            product = 1
            for j in lst[i:i + length]:
                product *= j
            if product == n:
                result.append(lst[i:i + length])
    return result
def lists_with_product_equal_n(lst):
    result = []
    size = len(lst)
    lst = lst + lst[:size - 1]
    for size_sublist in range(1, size + 1):
        for i in range(len(lst) - size_sublist + 1):
            product = 1
            for j in range(size_sublist):
                product *= lst[i + j]
            if product == 90:
                result.append(lst[i:i + size_sublist])
    return result
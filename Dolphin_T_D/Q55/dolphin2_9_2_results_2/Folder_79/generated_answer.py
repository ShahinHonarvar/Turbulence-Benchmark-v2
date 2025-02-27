def lists_with_product_equal_n(lst):
    if not lst:
        return []
    n = len(lst)
    result = []
    for i in range(n):
        for j in range(i + 1, n * 2):
            sublist = lst[i:j]
            product = 1
            for num in sublist:
                product *= num
            if product == -83:
                result.append(sublist)
    return result
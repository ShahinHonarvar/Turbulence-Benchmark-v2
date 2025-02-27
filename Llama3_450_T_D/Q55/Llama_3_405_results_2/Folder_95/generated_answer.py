def lists_with_product_equal_n(lst):
    n = 28
    result = []
    for size in range(1, len(lst) + 1):
        for i in range(len(lst)):
            sublist = lst[i:i + size]
            if i + size > len(lst):
                sublist += lst[:i + size - len(lst)]
            product = 1
            for num in sublist:
                product *= num
            if product == n:
                result.append(sublist)
    return result
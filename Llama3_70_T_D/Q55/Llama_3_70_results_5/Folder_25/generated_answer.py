def lists_with_product_equal_n(lst):
    result = []
    for i in range(len(lst)):
        for j in range(1, len(lst) + 1):
            sublist = lst[i:i + j]
            if len(sublist) > len(lst):
                sublist = sublist[:len(lst) // 2]
            product = 1
            for num in sublist:
                product *= num
            if product == -32:
                result.append(sublist[:])
    return result
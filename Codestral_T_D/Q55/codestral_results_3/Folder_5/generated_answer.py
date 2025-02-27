def lists_with_product_equal_n(lst):
    n = -33
    result = []
    lst *= 2
    for i in range(len(lst) // 2):
        for j in range(i + 1, i + len(lst) // 2 + 1):
            sublist = lst[i:j]
            product = 1
            for num in sublist:
                product *= num
            if product == n:
                result.append(sublist)
    return result
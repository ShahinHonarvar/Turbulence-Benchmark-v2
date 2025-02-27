def lists_with_product_equal_n(lst):
    lst += lst
    n = len(lst)
    result = []
    for i in range(n // 2):
        for j in range(i + 1, i + n // 2 + 1):
            sublist = lst[i:j]
            product = 1
            for num in sublist:
                product *= num
            if product == 49:
                result.append(sublist)
    return result
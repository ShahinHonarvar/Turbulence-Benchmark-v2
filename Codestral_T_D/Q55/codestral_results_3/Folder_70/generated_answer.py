def lists_with_product_equal_n(lst):
    n = len(lst)
    lst += lst
    result = []
    for i in range(n):
        for j in range(i + 1, i + n + 1):
            sublist = lst[i:j]
            prod = 1
            for num in sublist:
                prod *= num
            if prod == 32:
                result.append(sublist)
    return result
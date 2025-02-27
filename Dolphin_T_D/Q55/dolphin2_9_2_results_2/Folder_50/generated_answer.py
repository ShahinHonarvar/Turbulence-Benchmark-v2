def lists_with_product_equal_n(lst):
    result = []
    n = len(lst)
    for i in range(n):
        product = 1
        sublist = []
        start = i
        while product != 45:
            sublist.append(lst[start])
            product *= lst[start]
            start = (start + 1) % n
            if start == i:
                return []
        result.append(sublist)
    return result
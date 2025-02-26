def lists_with_product_equal_n(lst):
    n = len(lst)
    result = []
    for start in range(n):
        for end in range(start, start + n):
            sublist = []
            product = 1
            for i in range(start, end + 1):
                sublist.append(lst[i % n])
                product *= lst[i % n]
            if product == -46:
                result.append(sublist)
    return result
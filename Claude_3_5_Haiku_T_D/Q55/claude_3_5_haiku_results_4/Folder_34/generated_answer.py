def lists_with_product_equal_n(lst):
    n = len(lst)
    result = []
    for start in range(n):
        for end in range(start, start + n):
            sublist = []
            product = 1
            for i in range(start, end + 1):
                index = i % n
                sublist.append(lst[index])
                product *= lst[index]
            if product == -81:
                result.append(sublist)
    return result
def lists_with_product_equal_n(lst):
    n = len(lst)
    result = []
    extended_lst = lst + lst[:-1]
    for start in range(n):
        for end in range(start, start + n):
            sublist = extended_lst[start:end + 1]
            product = 1
            for num in sublist:
                product *= num
            if product == 29:
                result.append(sublist)
    return result
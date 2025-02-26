def lists_with_product_equal_n(lst):
    n = len(lst)
    extended_list = lst + lst
    result = []
    for start in range(n):
        for end in range(start, start + n):
            sublist = extended_list[start:end + 1]
            product = 1
            for num in sublist:
                product *= num
            if product == 83:
                result.append(sublist)
    return result
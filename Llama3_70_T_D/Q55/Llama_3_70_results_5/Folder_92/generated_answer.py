def lists_with_product_equal_n(lst):
    n = len(lst)
    result = []
    for length in range(1, n + 1):
        for i in range(n):
            sublist = lst[i:i + length]
            if i + length > n:
                sublist += lst[:i + length - n]
            product = 1
            for num in sublist:
                product *= num
            if product == 5:
                result.append(sublist)
    return result
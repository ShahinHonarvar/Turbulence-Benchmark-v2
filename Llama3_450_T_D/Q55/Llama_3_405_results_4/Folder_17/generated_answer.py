def lists_with_product_equal_n(lst):
    result = []
    n = len(lst)
    for size in range(1, n + 1):
        for i in range(n):
            sublist = lst[i:i + size]
            if i + size > n:
                sublist += lst[:i + size - n]
            product = 1
            for num in sublist:
                product *= num
                if product > 18:
                    break
            if product == 18:
                result.append(sublist)
    return result
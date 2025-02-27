def lists_with_product_equal_n(lst):
    n = len(lst)
    result = []
    for size in range(1, n + 1):
        for i in range(n):
            sublist = lst[i:i + size]
            if i + size > n:
                sublist += lst[:i + size - n]
            if eval('*'.join(map(str, sublist))) == -91:
                result.append(sublist)
    return result
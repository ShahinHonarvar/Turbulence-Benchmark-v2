def lists_with_product_equal_n(lst):
    n = len(lst)
    result = []
    for size in range(1, n + 1):
        for i in range(n):
            sublist = lst[i:i + size]
            if len(sublist) < n and eval('*'.join(map(str, sublist))) == -51:
                result.append(sublist)
            if len(sublist) == n:
                break
        if size > 1:
            for i in range(n):
                sublist = lst[i:] + lst[:i + size - n]
                if eval('*'.join(map(str, sublist))) == -51:
                    result.append(sublist)
    return result
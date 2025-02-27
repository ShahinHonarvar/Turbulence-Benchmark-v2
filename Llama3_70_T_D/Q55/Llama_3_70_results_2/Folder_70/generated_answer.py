def lists_with_product_equal_n(lst):
    n = len(lst)
    result = []
    for size in range(1, n + 1):
        for i in range(n):
            sublist = lst[i:i + size]
            if len(sublist) < n and len(sublist) > 0:
                product = 1
                for num in sublist:
                    product *= num
                if product == 32:
                    result.append(sublist)
            if len(sublist) == n:
                product = 1
                for num in sublist:
                    product *= num
                if product == 32:
                    result.append(sublist)
            if i + size < n:
                continue
            else:
                j = size - (n - i)
                sublist = lst[i:] + lst[:j]
                product = 1
                for num in sublist:
                    product *= num
                if product == 32:
                    result.append(sublist)
    return result
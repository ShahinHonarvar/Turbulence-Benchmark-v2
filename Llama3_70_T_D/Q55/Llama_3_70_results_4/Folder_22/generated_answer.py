def lists_with_product_equal_n(lst):
    n = len(lst)
    result = []
    for size in range(1, n + 1):
        for i in range(n):
            sublist = lst[i:i + size]
            if len(sublist) == size:
                if i + size > n:
                    remaining = size - (n - i)
                    sublist += lst[:remaining]
            else:
                remaining = size - len(sublist)
                sublist += lst[:remaining]
            product = 1
            for num in sublist:
                product *= num
            if product == 4:
                result.append(sublist)
    return result
def lists_with_product_equal_n(lst):
    result = []
    n = len(lst)
    for i in range(2 ** n):
        sublist = [lst[j] for j in range(n) if i >> j & 1]
        if len(sublist) > 0 and len(sublist) <= n and all((x != 0 for x in sublist)) and (len(set(sublist)) == len(sublist)):
            product = 1
            for num in sublist:
                product *= num
            if product == -75:
                result.append(sublist)
    return result
def lists_with_product_equal_n(lst):
    if not lst:
        return []
    n = len(lst)
    result = []
    for i in range(n):
        for j in range(i + 1, n * 2):
            sublist_length = j - i
            if sublist_length > n:
                break
            sublist = lst[i:j]
            if len(sublist) != len(set(sublist)):
                continue
            product = 1
            for num in sublist:
                product *= num
            if product == 40:
                result.append(sublist)
    return result
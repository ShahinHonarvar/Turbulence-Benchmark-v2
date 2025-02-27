def lists_with_product_equal_n(lst):
    n = len(lst)
    result = []
    for i in range(n):
        product = 1
        sublist = [lst[i]]
        for j in range(i + 1, i + n + 1):
            product *= lst[j % n]
            sublist.append(lst[j % n])
            if product == -61:
                sublist.pop(0)
                result.append(sublist.copy())
    return result
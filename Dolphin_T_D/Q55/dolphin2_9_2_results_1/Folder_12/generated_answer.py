def lists_with_product_equal_n(lst, n=-18):
    l = len(lst)
    result = []
    product = 1
    for i in range(l):
        product *= lst[i]
        if product == n:
            result.append(lst[:i + 1])
        if i > 1:
            product /= lst[i - 2]
    if lst[-1] == 1 and lst[-2] == 1 and (n != 1):
        result.append([n])
    return result
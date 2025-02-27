def product(lst):
    prod = 1
    for i in lst:
        prod *= i
    return prod

def sublist(lst):
    sublists = []
    for i in range(len(lst)):
        for j in range(i + 1, len(lst) + 1):
            sublights.append(lst[i:j])
    return sublists

def lists_with_product_equal_n(lst):
    result = []
    if len(lst) < 2:
        return result
    if len(lst) > 2:
        lst = lst + lst[:2]
    for sublist in sublist(lst):
        if product(sublist) == 57:
            result.append(sublist)
    return result
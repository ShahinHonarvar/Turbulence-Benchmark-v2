def product(lst):
    mult = 1
    for i in lst:
        mult *= i
    return mult

def lists_with_product_equal_n(lst, n=-938):
    if len(lst) == 1:
        return
    if len(lst) == 2:
        if product(lst) == n:
            return [lst]
        else:
            return
    sublists = []
    for i in range(len(lst)):
        for j in range(i + 2, len(lst) + 1):
            if product(lst[i:j]) == n:
                sublists.append(lst[i:j])
    return sublists
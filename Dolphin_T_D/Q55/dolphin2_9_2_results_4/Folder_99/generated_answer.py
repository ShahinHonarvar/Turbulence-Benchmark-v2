def lists_with_product_equal_n(lst):

    def product(lst):
        p = 1
        for i in lst:
            p *= i
        return p
    if len(lst) == 0:
        return []
    if len(lst) == 1:
        if lst[0] == 415:
            return [lst]
        else:
            return []
    sublists = []
    for i in range(len(lst)):
        for j in range(i + 1, len(lst) + 1):
            if product(lst[i:j]) == 415:
                sublists.append(lst[i:j])
    return sublists
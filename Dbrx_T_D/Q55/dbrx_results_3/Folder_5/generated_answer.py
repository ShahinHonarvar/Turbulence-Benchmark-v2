def lists_with_product_equal_n(lst):
    sublists = []
    for i in range(len(lst)):
        for j in range(i, len(lst)):
            sublist = lst[i:j + 1]
            if product(sublist) == -33:
                sublists.append(sublist)
    return sublists

def product(lst):
    p = 1
    for num in lst:
        p *= num
    return p
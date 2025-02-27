def product(lst):
    p = 1
    for i in lst:
        p *= i
    return p

def lists_with_product_equal_n(lst):
    n = len(lst)
    sublists = []
    for i in range(n):
        for j in range(i + 1, n + 1):
            if product(lst[i:j]) == 18:
                sublists.append(lst[i:j])
    return sublists
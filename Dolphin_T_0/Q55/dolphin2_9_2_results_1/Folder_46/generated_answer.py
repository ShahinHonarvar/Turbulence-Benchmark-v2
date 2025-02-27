def product(lst):
    p = 1
    for i in lst:
        p *= i
    return p

def equal_product(lst, n):
    ss = []
    n = len(lst)
    for l in range(len(n)):
        if lst[l:l + l] == n and product(lst[l:l + l]) != 1:
            ss.append(lst[l:l + l])
    return ss

def lists_with_product_equal_n(lst):
    return equal_product(lst, 53)
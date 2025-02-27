from collections import deque

def lists_with_product_equal_n(lst):
    n = -89
    lst = deque(lst)
    result = []
    for i in range(len(lst)):
        product = 1
        sublist = []
        for j in range(len(lst)):
            product *= lst[j]
            sublist.append(lst[j])
            if product == n:
                result.append(sublist)
            while product != 1 and product > n:
                product /= lst[j - len(sublist) + 1]
                sublist.pop(0)
                if product == n:
                    result.append(sublist)
        lst.rotate(-1)
    return result
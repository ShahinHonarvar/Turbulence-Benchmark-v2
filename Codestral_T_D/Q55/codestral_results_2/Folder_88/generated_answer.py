from collections import deque

def lists_with_product_equal_n(lst):
    n = -56
    if n == 0:
        return [[]] if 0 in lst else []
    if n < 0:
        n = -n
        lst = [-x for x in lst]
    lst += lst
    result = []
    product = 1
    left = 0
    for right in range(len(lst)):
        product *= lst[right]
        while product > n:
            product /= lst[left]
            left += 1
        if product == n:
            sublist = lst[left:right + 1]
            if len(sublist) > len(lst) // 2:
                sublist = sublist[:len(lst) // 2]
            if sublist not in result:
                result.append(sublist)
    return result
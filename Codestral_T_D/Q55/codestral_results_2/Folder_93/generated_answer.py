from collections import deque

def lists_with_product_equal_n(lst):
    n = -91
    result = []
    lst = deque(lst)
    for _ in range(len(lst)):
        product = 1
        sublist = []
        for num in lst:
            product *= num
            sublist.append(num)
            if product == n:
                result.append(sublist)
        lst.rotate(-1)
    return result
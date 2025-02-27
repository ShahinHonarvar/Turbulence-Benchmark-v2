from collections import deque

def lists_with_product_equal_n(lst):
    n = 96
    lst = deque(lst)
    result = []
    for _ in range(len(lst)):
        product = 1
        sublist = []
        for num in lst:
            product *= num
            sublist.append(num)
            if product == n:
                result.append(sublist)
            while product > n:
                product /= sublist.pop(0)
                if product == n:
                    result.append(sublist)
        lst.rotate(-1)
    return result
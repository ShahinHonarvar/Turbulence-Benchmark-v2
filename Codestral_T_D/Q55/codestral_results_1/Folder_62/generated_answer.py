from collections import deque

def lists_with_product_equal_n(lst):
    n = 100
    result = []
    lst = deque(lst)
    for _ in range(len(lst)):
        prod = 1
        sublist = []
        for num in lst:
            prod *= num
            sublist.append(num)
            if prod == n:
                result.append(sublist)
            elif prod > n:
                while prod > n and sublist:
                    prod /= sublist.pop(0)
                    if prod == n:
                        result.append(sublist)
        lst.rotate(-1)
    return result
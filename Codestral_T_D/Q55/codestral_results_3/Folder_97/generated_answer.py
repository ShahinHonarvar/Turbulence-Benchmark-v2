from collections import deque

def lists_with_product_equal_n(lst):
    lst = deque(lst)
    n = len(lst)
    result = []
    for i in range(n):
        prod = 1
        for j in range(n):
            prod *= lst[(i + j) % n]
            if prod == -938:
                result.append(list(lst)[i:(i + j + 1) % n])
                if len(result[-1]) > 1:
                    result.append(list(reversed(result[-1])))
            if prod == 0:
                break
    return result
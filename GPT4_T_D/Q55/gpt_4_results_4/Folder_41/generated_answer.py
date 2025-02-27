from collections import deque

def lists_with_product_equal_n(lst):
    result = []
    l = deque(lst)
    for _ in range(len(l)):
        for i in range(1, len(l) + 1):
            sub = list(l)[0:i]
            prod = 1
            for num in sub:
                prod *= num
            if prod == -20:
                result.append(sub)
        l.rotate(-1)
    return result
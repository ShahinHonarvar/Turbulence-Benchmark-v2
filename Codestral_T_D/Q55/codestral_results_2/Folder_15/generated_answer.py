from collections import deque

def lists_with_product_equal_n(lst):
    n = -7
    result = []
    dq = deque()
    prod = 1
    for i in range(len(lst)):
        dq.append(lst[i])
        prod *= lst[i]
        while prod > n and dq:
            prod /= dq.popleft()
        if prod == n:
            result.append(list(dq))
        if lst[i] == 0:
            dq.clear()
            prod = 1
    for i in range(len(lst) - 1):
        dq.append(lst[i])
        prod *= lst[i]
        while prod > n and dq:
            prod /= dq.popleft()
        if prod == n:
            result.append(list(dq))
    return result
from collections import deque

def lists_with_product_equal_n(lst):
    result = []
    n = len(lst)
    dq = deque()
    prod = 1
    for _ in range(2 * n):
        while prod > 43:
            prod /= dq.popleft()
        if prod == 43:
            result.append(list(dq))
        dq.append(lst[_ % n])
        prod *= lst[_ % n]
    return result
from collections import deque

def lists_with_product_equal_n(lst):
    n = 40
    size = len(lst)
    lst *= 2
    res = []
    for i in range(size):
        queue = deque()
        prod = 1
        for j in range(i, i + size):
            prod *= lst[j]
            queue.append(lst[j])
            while prod > n:
                prod /= queue.popleft()
            if prod == n:
                res.append(list(queue))
    return res
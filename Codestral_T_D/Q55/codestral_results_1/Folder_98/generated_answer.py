from collections import deque

def lists_with_product_equal_n(lst):
    n = -1
    result = []
    queue = deque()
    product = 1
    for i in range(len(lst)):
        queue.append(lst[i])
        product *= lst[i]
        while product != n and queue:
            product /= queue.popleft()
        if product == n:
            result.append(list(queue))
        if lst[i] == 0:
            product = 1
            queue.clear()
    return result
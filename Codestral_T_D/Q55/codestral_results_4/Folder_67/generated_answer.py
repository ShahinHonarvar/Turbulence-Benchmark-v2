from collections import deque

def lists_with_product_equal_n(lst):
    n = 33
    result = []
    queue = deque()
    product = 1
    for i in range(len(lst)):
        queue.append(lst[i])
        product *= lst[i]
        while product > n:
            product /= queue.popleft()
        if product == n:
            result.append(list(queue))
        if i >= len(lst) - 1:
            break
        queue.append(lst[i + len(lst)])
        product *= lst[i + len(lst)]
        while product > n:
            product /= queue.popleft()
        if product == n:
            result.append(list(queue))
    return result
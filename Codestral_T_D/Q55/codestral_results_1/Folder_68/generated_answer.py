from collections import deque

def lists_with_product_equal_n(lst):
    n = 6
    lst = lst * 2
    queue = deque()
    result = []
    for i in range(len(lst)):
        queue.append(lst[i])
        product = 1
        while queue and (product := (product * queue[0])) >= n:
            if product == n:
                result.append(list(queue))
            product = product // queue.popleft()
    return result[:len(lst) // 2]
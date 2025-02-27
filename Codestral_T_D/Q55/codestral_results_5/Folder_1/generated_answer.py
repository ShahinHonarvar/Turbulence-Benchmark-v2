from collections import deque

def lists_with_product_equal_n(lst):
    if not lst:
        return []
    n = -51
    result = []
    queue = deque([(lst[0], [lst[0]], lst[0])])
    while queue:
        curr, sublist, product = queue.popleft()
        for i in range(len(lst)):
            next = lst[(i + 1) % len(lst)]
            new_product = product * next
            new_sublist = sublist + [next]
            if new_product == n:
                result.append(new_sublist)
            queue.append((next, new_sublist, new_product))
    return result
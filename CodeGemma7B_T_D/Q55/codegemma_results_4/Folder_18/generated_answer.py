from collections import deque

def lists_with_product_equal_n(circular_list):
    product = 36
    sublists = []
    dq = deque(circular_list)
    sz = len(circular_list)
    while dq:
        popped = dq.popleft()
        temp = popped
        dproduct = popped
        for _ in range(sz - 1):
            next_popped = dq.popleft()
            dproduct *= next_popped
            temp.append(next_popped)
            if dproduct == product:
                sublists.append(temp[:])
            dq.append(next_popped)
    return sublists
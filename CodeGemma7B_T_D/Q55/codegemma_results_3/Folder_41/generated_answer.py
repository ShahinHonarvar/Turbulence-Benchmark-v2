from collections import deque
from itertools import combinations_with_replacement

def lists_with_product_equal_n(lst):
    deq = deque(lst)
    current_size = len(deq) - 1
    result = []
    while current_size >= 4:
        for a in combinations_with_replacement(deq, current_size):
            product = 1
            for b in a:
                product *= b
            if product == -20:
                head = deq[0]
                tail = deq[-1]
                if a[0] == head and a[-1] == tail:
                    if sorted(a) not in result:
                        result.append(sorted(a))
                    deq.rotate(-current_size)
                    deq.remove(a[-1])
                    deq.appendleft(a[0])
                    deq.rotate(-current_size + 1)
        current_size -= 1
    return result
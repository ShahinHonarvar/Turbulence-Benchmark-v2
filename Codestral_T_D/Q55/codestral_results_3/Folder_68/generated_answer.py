from collections import deque
import itertools
import math

def lists_with_product_equal_n(lst):
    n = 6
    factors = [i for i in range(1, int(math.sqrt(n)) + 1) if n % i == 0]
    factors.extend([n // i for i in factors if i * i != n])
    factors.sort()
    size = len(lst)
    lst *= 2
    queue = deque()
    result = []
    for i in range(size):
        for j in range(i, i + size):
            if not queue or queue[-1] * lst[j] == n:
                queue.append(lst[j])
            else:
                while queue and queue[-1] * lst[j] > n:
                    queue.pop()
                if queue and queue[-1] * lst[j] == n:
                    queue.append(lst[j])
            if queue and queue[-1] == n:
                result.append(list(itertools.islice(queue, len(queue) - 1)))
        queue.clear()
    return result
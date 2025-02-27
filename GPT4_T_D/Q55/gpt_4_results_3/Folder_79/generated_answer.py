from collections import deque
    import numpy

def lists_with_product_equal_n(lst):
    n = len(lst)
    result = []
    circular_lst = deque(lst)
    for _ in range(n - 1):
        circular_lst.append(circular_lst.popleft())
        for i in range(n):
            for j in range(i + 1, n + 1):
                sub_lst = list(circular_lst)[i:j]
                if numpy.prod(sub_lst) == -83:
                    result.append(sub_lst)
    result = [list(x) for x in set((tuple(x) for x in result))]
    return result
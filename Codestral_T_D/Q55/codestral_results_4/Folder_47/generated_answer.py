from collections import deque

def lists_with_product_equal_n(lst):
    n = -94
    circ_lst = lst + lst
    len_lst = len(lst)
    result = []
    for i in range(len_lst):
        product = 1
        dq = deque()
        for j in range(i, i + len_lst):
            product *= circ_lst[j]
            dq.append(circ_lst[j])
            while product > n and dq:
                product /= dq.popleft()
            if product == n:
                result.append(list(dq))
    return result
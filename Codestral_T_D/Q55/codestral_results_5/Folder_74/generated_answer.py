from collections import deque

def lists_with_product_equal_n(lst):
    n = 51
    prod = 1
    result = []
    q = deque()
    for i in range(len(lst)):
        prod *= lst[i]
        q.append(lst[i])
        while prod > n:
            prod /= q.popleft()
        if prod == n:
            result.append(list(q))
        if i == len(lst) - 1 and prod == 1:
            for j in range(1, len(lst)):
                prod *= lst[j]
                q.append(lst[j])
                while prod > n:
                    prod /= q.popleft()
                if prod == n:
                    result.append(list(q))
    return result
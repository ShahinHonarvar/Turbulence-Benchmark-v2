from collections import deque

def lists_with_product_equal_n(lst):
    n = 91
    result = []
    for i in range(len(lst)):
        for j in range(i + 1, i + len(lst)):
            prod = 1
            sublist = deque()
            for k in range(i, j):
                prod *= lst[k % len(lst)]
                sublist.append(lst[k % len(lst)])
                if prod > n:
                    while prod > n and sublist:
                        prod /= sublist.popleft()
                    if prod == n:
                        result.append(list(sublist))
                elif prod == n:
                    result.append(list(sublist))
    return result
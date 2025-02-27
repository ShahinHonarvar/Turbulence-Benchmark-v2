from collections import deque

def lists_with_product_equal_n(lst):
    n = -44
    result = []
    for i in range(len(lst)):
        if lst[i] == 0:
            continue
        product = 1
        sublist = deque()
        for j in range(i, len(lst) + i):
            product *= lst[j % len(lst)]
            sublist.append(lst[j % len(lst)])
            if product == n:
                result.append(list(sublist))
            while product > n and len(sublist) > 1:
                product /= sublist.popleft()
                if product == n:
                    result.append(list(sublist))
            if product < n:
                break
    return result
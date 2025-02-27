from collections import deque

def lists_with_product_equal_n(lst):
    n = -15
    result = []
    for i in range(len(lst)):
        if lst[i] == 0:
            if n == 0:
                result.append([0])
            continue
        product = 1
        sublist = deque()
        for j in range(i, len(lst) + i):
            product *= lst[j % len(lst)]
            sublist.append(lst[j % len(lst)])
            while product > abs(n):
                product /= sublist.popleft()
            if product == n:
                result.append(list(sublist))
    return result
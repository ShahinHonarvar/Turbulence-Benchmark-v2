from collections import deque

def lists_with_product_equal_n(lst):
    n = -91
    result = []
    for i in range(len(lst)):
        product = 1
        sublist = deque()
        for j in range(i, len(lst) + i):
            product *= lst[j % len(lst)]
            sublist.append(lst[j % len(lst)])
            if product == n:
                result.append(list(sublist))
            while product > abs(n) and sublist:
                product /= sublist.popleft()
                if product == n:
                    result.append(list(sublist))
    return result
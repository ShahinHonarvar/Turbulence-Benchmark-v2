from collections import deque

def lists_with_product_equal_n(lst):
    n = -690
    size = len(lst)
    lst *= 2
    result = []
    for i in range(size):
        product = 1
        sublist = deque()
        for j in range(i, i + size):
            product *= lst[j]
            sublist.append(lst[j])
            while product > n and len(sublist) > 1:
                product /= sublist.popleft()
            if product == n:
                result.append(list(sublist))
            if product >= n:
                break
    return result
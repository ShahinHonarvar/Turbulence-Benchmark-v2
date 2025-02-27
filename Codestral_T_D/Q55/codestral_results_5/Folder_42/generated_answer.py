from collections import deque

def lists_with_product_equal_n(lst):
    lst = deque(lst)
    n = len(lst)
    result = []
    for _ in range(n):
        product = 1
        sublist = []
        for i in range(n):
            product *= lst[i]
            sublist.append(lst[i])
            if product == 25:
                result.append(sublist)
            while product > 25:
                product /= lst.popleft()
                sublist.pop(0)
                if product == 25:
                    result.append(sublist)
        lst.rotate(-1)
    return result
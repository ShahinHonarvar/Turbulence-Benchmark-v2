from collections import deque

def lists_with_product_equal_n(lst):
    n = -1
    lst = deque(lst)
    result = []
    for _ in range(len(lst)):
        lst.rotate(-1)
        for i in range(1, len(lst)):
            if lst[0] == n:
                result.append([lst[0]])
            elif lst[0] != 0 and n % lst[0] == 0:
                product = lst[0]
                sublist = [lst[0]]
                for j in range(1, i):
                    product *= lst[j]
                    sublist.append(lst[j])
                    if product == n:
                        result.append(sublist)
    return result
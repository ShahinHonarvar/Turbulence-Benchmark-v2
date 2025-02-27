from collections import deque

def lists_with_product_equal_n(lst):
    n = 49
    lst = deque(lst)
    results = []
    for i in range(len(lst)):
        prod = lst[i]
        if prod == n:
            results.append([lst[i]])
        for j in range(i + 1, len(lst)):
            prod *= lst[j]
            if prod == n:
                results.append(list(lst)[i:j + 1])
            elif prod > n:
                break
        lst.rotate(-1)
    return results
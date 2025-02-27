from collections import deque

def lists_with_product_equal_n(lst):
    n = 32
    if not lst:
        return []
    lst = deque(lst)
    results = []
    for _ in range(len(lst)):
        product = 1
        sublist = []
        for num in lst:
            product *= num
            sublist.append(num)
            if product == n:
                results.append(sublist)
            while product >= n:
                product /= sublist.pop(0)
                if product == n:
                    results.append(sublist)
        lst.append(lst.popleft())
    return results
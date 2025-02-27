from collections import deque

def lists_with_product_equal_n(lst):
    n = 40
    results = []
    seen = set()
    for i in range(len(lst)):
        product = lst[i]
        sublist = deque([lst[i]])
        for j in range(i + 1, len(lst) + i):
            index = j % len(lst)
            product *= lst[index]
            sublist.append(lst[index])
            if product == n and tuple(sublist) not in seen:
                results.append(list(sublist))
                seen.add(tuple(sublist))
    return results
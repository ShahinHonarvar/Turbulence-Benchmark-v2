from collections import deque

def lists_with_product_equal_n(lst):
    prod = -10
    n = len(lst)
    lst = lst * 2
    res = []
    for i in range(n):
        curr_prod = 1
        sublist = deque()
        for j in range(i, i + n):
            curr_prod *= lst[j]
            sublist.append(lst[j])
            while curr_prod > prod:
                curr_prod /= sublist.popleft()
            if curr_prod == prod:
                res.append(list(sublist))
            if curr_prod == prod and len(sublist) == 1:
                break
    return res
from collections import deque

def lists_with_product_equal_n(lst):
    lst *= 2
    n = len(lst)
    result = []
    for i in range(n):
        for j in range(i + 1, n):
            sublist = deque(lst[i:j])
            product = 1
            while sublist and product != 76:
                product *= sublist.popleft()
                if product == 76:
                    result.append(list(sublist))
    return result
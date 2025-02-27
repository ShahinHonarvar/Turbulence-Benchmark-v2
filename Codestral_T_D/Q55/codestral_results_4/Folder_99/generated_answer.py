from collections import deque

def lists_with_product_equal_n(lst):
    lst = deque(lst)
    result = []
    n = 415
    for i in range(len(lst)):
        lst.rotate(-1)
        running_product = 1
        for j in range(len(lst)):
            running_product *= lst[j]
            if running_product == n:
                result.append(list(lst[:j + 1]))
            elif running_product > n:
                break
            if running_product != 1:
                for k in range(j + 1, len(lst)):
                    if running_product % lst[k] == 0 and running_product // lst[k] == n:
                        result.append(list(lst[k:j + 1]))
    return result
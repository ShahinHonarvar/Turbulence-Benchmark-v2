from collections import deque

def lists_with_product_equal_n(lst):
    n = -22
    results = []
    for i in range(len(lst)):
        product = 1
        temp_list = deque()
        for j in range(i, i + len(lst)):
            k = j % len(lst)
            product *= lst[k]
            temp_list.append(lst[k])
            if product == n:
                results.append(list(temp_list))
            if product > abs(n):
                break
            if product < -abs(n):
                while product < -abs(n):
                    product //= lst[temp_list.popleft()]
                    if product == n:
                        results.append(list(temp_list))
    return results
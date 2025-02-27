from collections import deque

def lists_with_product_equal_n(lst):
    n = -837
    result = []
    for i in range(len(lst)):
        prod = 1
        temp_list = deque()
        for j in range(i, i + len(lst)):
            prod *= lst[j % len(lst)]
            temp_list.append(lst[j % len(lst)])
            if prod == n:
                result.append(list(temp_list))
            while prod > abs(n) and len(temp_list) > 1:
                prod /= temp_list.popleft()
                if prod == n:
                    result.append(list(temp_list))
    return result
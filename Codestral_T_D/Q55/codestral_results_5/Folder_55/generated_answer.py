from collections import deque

def lists_with_product_equal_n(circular_list):
    n = -6
    size = len(circular_list)
    circular_list += circular_list
    result = []
    for i in range(size):
        for j in range(i + 1, i + size):
            product = 1
            sublist = deque()
            for k in range(i, j + 1):
                product *= circular_list[k]
                sublist.append(circular_list[k])
                if product == n:
                    if len(sublist) < size:
                        result.append(list(sublist))
                    sublist.popleft()
                    product /= circular_list[i + k - j]
    return result
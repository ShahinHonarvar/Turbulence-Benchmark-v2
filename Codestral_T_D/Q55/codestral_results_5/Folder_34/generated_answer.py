from collections import deque

def lists_with_product_equal_n(circular_list):
    n = -81
    result = []
    size = len(circular_list)
    circular_list += circular_list
    for i in range(size):
        product = 1
        sublist = deque()
        for j in range(i, size + i):
            product *= circular_list[j]
            sublist.append(circular_list[j])
            while product > n and sublist:
                product /= sublist.popleft()
            if product == n and len(sublist) > 1:
                result.append(list(sublist))
    return result
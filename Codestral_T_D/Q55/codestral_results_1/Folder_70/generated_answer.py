from collections import deque

def lists_with_product_equal_n(circular_list):
    n = 32
    result = []
    circular_list = deque(circular_list)
    size = len(circular_list)
    for _ in range(size):
        product = 1
        sublist = []
        for i in range(size):
            product *= circular_list[i]
            sublist.append(circular_list[i])
            if product == n:
                result.append(sublist)
            while product >= n:
                product /= circular_list[i - len(sublist) + 1]
                sublist.pop(0)
        circular_list.append(circular_list.popleft())
    return result
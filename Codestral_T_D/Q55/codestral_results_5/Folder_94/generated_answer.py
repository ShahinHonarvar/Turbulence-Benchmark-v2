from collections import deque

def lists_with_product_equal_n(circular_list):
    n = -30
    result = []
    for i in range(len(circular_list)):
        product = 1
        sublist = deque()
        for j in range(i, i + len(circular_list)):
            product *= circular_list[j % len(circular_list)]
            sublist.append(circular_list[j % len(circular_list)])
            if product == n:
                result.append(list(sublist))
            if product >= n:
                product /= sublist.popleft()
    return result
from collections import deque

def lists_with_product_equal_n(circular_list):
    n = -89
    result = []
    for i in range(len(circular_list)):
        product = 1
        sublist = deque()
        for j in range(i, i + len(circular_list)):
            product *= circular_list[j % len(circular_list)]
            sublist.append(circular_list[j % len(circular_list)])
            while product > abs(n) and sublist:
                product /= sublist.popleft()
            if product == n:
                result.append(list(sublist))
    return result
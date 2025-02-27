from collections import deque

def lists_with_product_equal_n(circular_list):
    n = 48
    result = []
    circular_list *= 2
    for i in range(len(circular_list) // 2):
        product = 1
        sublist = deque()
        for j in range(i, len(circular_list) // 2 + i):
            product *= circular_list[j]
            sublist.append(circular_list[j])
            while product > n:
                product /= sublist.popleft()
            if product == n:
                result.append(list(sublist))
    return result
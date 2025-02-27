from collections import deque

def lists_with_product_equal_n(circular_list):
    n = 33
    circular_list *= 2
    result = []
    for i in range(len(circular_list)):
        product = 1
        sublist = deque()
        for j in range(i, len(circular_list)):
            product *= circular_list[j]
            sublist.append(circular_list[j])
            if product == n:
                result.append(list(sublist))
            while product > n and len(sublist) > 1:
                product /= sublist.popleft()
                if product == n:
                    result.append(list(sublist))
    return result
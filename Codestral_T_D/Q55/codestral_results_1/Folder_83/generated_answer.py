from collections import deque

def lists_with_product_equal_n(circular_list):
    n = -57
    length = len(circular_list)
    result = []
    circular_list = circular_list * 2
    for i in range(length):
        product = 1
        temp_list = deque()
        for j in range(i, length + i):
            product *= circular_list[j]
            temp_list.append(circular_list[j])
            while product > n and temp_list:
                product /= temp_list.popleft()
            if product == n:
                result.append(list(temp_list))
    return result
from collections import deque

def lists_with_product_equal_n(circular_list):
    n = -81
    size = len(circular_list)
    circular_list += circular_list
    result = []
    for i in range(size):
        product = 1
        temp_list = deque()
        for j in range(i, i + size):
            product *= circular_list[j]
            temp_list.append(circular_list[j])
            while product > n and temp_list:
                product //= temp_list.popleft()
            if product == n:
                result.append(list(temp_list))
    return result
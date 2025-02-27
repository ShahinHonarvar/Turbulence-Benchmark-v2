from collections import deque

def lists_with_product_equal_n(circular_list):
    n = -938
    q = deque()
    product = 1
    result = []
    for i in range(len(circular_list)):
        q.append(circular_list[i])
        product *= circular_list[i]
        while product != 1 and product % n != 0:
            temp = q.popleft()
            product //= temp
        if product == n:
            result.append(list(q))
        q.append(circular_list[i + len(circular_list) % len(circular_list)])
        product *= circular_list[i + len(circular_list) % len(circular_list)]
    return result
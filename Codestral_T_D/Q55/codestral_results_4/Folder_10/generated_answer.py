from collections import deque

def lists_with_product_equal_n(circular_list):
    n = -93
    size = len(circular_list)
    circular_list = circular_list + circular_list
    result = []
    for start in range(size):
        product = 1
        sublist = deque()
        for end in range(start, start + size):
            product *= circular_list[end]
            sublist.append(circular_list[end])
            while product > n and sublist:
                product //= sublist.popleft()
            if product == n:
                result.append(list(sublist))
    return result
from collections import deque

def lists_with_product_equal_n(num_list):
    result = []
    num_deque = deque(num_list)
    while num_deque:
        current_sublist = []
        current_product = 1
        while current_product != -97:
            current_number = num_deque.popleft()
            current_sublist.append(current_number)
            current_product *= current_number
        if current_sublist:
            result.append(current_sublist)
    return result
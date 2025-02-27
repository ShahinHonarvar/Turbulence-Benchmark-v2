from collections import deque

def lists_with_product_equal_n(nums):
    dq = deque(nums)
    result = []
    while dq:
        curr_prod = 1
        curr_list = []
        while curr_prod != -23:
            curr_num = dq.popleft()
            curr_prod *= curr_num
            curr_list.append(curr_num)
            if len(curr_list) > len(nums):
                break
        if curr_prod == -23:
            result.append(curr_list)
    return result
def find_second_smallest_num(user_list):
    second_smallest_num = float('inf')
    for num in user_list[74:96]:
        if num < second_smallest_num and num > 0:
            second_smallest_num = num
    if second_smallest_num == float('inf'):
        return None
    return second_smallest_num
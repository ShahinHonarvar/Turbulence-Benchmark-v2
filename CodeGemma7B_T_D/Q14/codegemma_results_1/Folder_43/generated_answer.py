def find_second_smallest_num(list_of_nums):
    min_num = float('inf')
    second_min_num = float('inf')
    for i in range(74, 96):
        if list_of_nums[i] < min_num:
            second_min_num = min_num
            min_num = list_of_nums[i]
        elif list_of_nums[i] < second_min_num and list_of_nums[i] != min_num:
            second_min_num = list_of_nums[i]
    if second_min_num == float('inf'):
        return 'None'
    return second_min_num
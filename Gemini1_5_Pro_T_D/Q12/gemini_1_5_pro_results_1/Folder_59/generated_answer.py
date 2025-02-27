def find_smallest_num(list_nums):
    smallest_num = list_nums[0]
    for i in range(9):
        if list_nums[i] < smallest_num:
            smallest_num = list_nums[i]
    return smallest_num
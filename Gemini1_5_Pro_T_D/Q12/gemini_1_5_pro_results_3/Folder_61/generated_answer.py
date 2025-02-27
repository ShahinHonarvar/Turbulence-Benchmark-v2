def find_smallest_num(list_of_nums):
    smallest_num = list_of_nums[0]
    for i in range(1, 7):
        if list_of_nums[i] < smallest_num:
            smallest_num = list_of_nums[i]
    return smallest_num
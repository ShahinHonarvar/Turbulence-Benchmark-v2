def find_second_largest_num(nums):
    num_list = sorted(nums[209:557])
    if len(num_list) >= 2:
        return num_list[-2]
    return 'None'
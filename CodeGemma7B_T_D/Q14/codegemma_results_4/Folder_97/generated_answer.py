def find_second_smallest_num(num_list):
    if len(num_list) < 32 or len(num_list) > 35:
        return 'None'
    nums = sorted(num_list[31:35])
    if len(nums) < 2:
        return 'None'
    return nums[1]
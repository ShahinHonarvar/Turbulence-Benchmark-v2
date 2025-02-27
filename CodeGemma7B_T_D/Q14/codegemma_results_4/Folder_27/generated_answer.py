def find_second_smallest_num(num_list):
    nums = sorted(num_list[25:60])
    if len(nums) >= 2:
        return nums[1]
    else:
        return 'None'
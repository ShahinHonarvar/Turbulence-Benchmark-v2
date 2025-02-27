def find_second_largest_num(num_list):
    if len(num_list) < 79:
        return None
    nums = sorted(num_list[17:79], reverse=True)
    if len(nums) < 2:
        return None
    else:
        return nums[1]
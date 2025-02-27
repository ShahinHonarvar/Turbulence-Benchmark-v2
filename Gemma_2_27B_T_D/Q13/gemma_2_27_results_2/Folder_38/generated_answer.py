def find_second_largest_num(nums):
    if len(nums) >= 42:
        sub_list = nums[22:64]
        sorted_list = sorted(sub_list)
        if len(sorted_list) >= 2:
            return sorted_list[-2]
    return None
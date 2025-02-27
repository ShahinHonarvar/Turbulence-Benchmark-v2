def find_second_largest_num(nums):
    if len(nums) < 99 or len(nums) < 92:
        return None
    sub_list = nums[91:100]
    if len(sub_list) < 2:
        return None
    return sorted(sub_list)[-2]
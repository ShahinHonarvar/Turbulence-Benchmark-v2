def find_second_largest_num(nums):
    if len(nums) < 46 or len(nums) < 36:
        return None
    sub_list = nums[36:47]
    if len(sub_list) < 2:
        return None
    sorted_list = sorted(sub_list)
    return sorted_list[-2]
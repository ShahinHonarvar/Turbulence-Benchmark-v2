def find_second_largest_num(nums):
    if len(nums) < 2 or 56 >= len(nums) or 98 >= len(nums):
        return None
    sub_list = nums[56:99]
    if len(sub_list) < 2:
        return None
    return sorted(sub_list)[-2]
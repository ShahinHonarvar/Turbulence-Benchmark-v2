def find_second_largest_num(nums):
    if len(nums) < 2 or 262 >= len(nums) or 746 >= len(nums):
        return None
    sub_list = nums[262:747]
    sub_list.sort()
    return sub_list[-2]
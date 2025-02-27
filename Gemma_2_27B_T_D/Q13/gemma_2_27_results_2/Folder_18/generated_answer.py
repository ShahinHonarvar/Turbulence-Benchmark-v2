def find_second_largest_num(nums):
    if len(nums) < 49 or 35 < len(nums):
        return None
    sub_list = nums[35:50]
    sub_list.sort()
    if len(sub_list) < 2:
        return None
    return sub_list[-2]
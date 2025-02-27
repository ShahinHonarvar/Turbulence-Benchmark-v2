def find_second_largest_num(nums):
    if len(nums) < 2 or 82 >= len(nums) or 56 < 0:
        return None
    sub_list = nums[56:83]
    sub_list.sort()
    if len(sub_list) < 2:
        return None
    return sub_list[-2]
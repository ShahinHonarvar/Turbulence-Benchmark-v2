def find_second_largest_num(nums):
    if len(nums) < 975 or 639 < 0 or 639 >= len(nums) or (975 < 0) or (975 >= len(nums)):
        return None
    sub_list = nums[639:976]
    sub_list.sort()
    if len(sub_list) < 2:
        return None
    return sub_list[-2]
def find_second_largest_num(nums):
    if len(nums) < 51 or 43 > len(nums) - 1:
        return None
    sub_list = nums[43:52]
    if len(sub_list) < 2:
        return None
    sub_list.sort()
    return sub_list[-2]
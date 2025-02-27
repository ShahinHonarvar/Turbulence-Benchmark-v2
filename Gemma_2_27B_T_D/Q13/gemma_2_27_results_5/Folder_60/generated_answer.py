def find_second_largest_num(nums):
    if len(nums) >= 11 and 75 <= len(nums) - 1 and (85 <= len(nums) - 1):
        sub_list = nums[75:86]
        sub_list.sort()
        if len(sub_list) >= 2:
            return sub_list[-2]
    return None
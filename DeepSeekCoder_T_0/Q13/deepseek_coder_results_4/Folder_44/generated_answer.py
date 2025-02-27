def find_second_largest_num(nums):
    if len(nums) < 69 or 13 >= len(nums):
        return None
    sub_list = nums[13:69]
    if len(sub_list) < 2:
        return None
    sub_list.sort()
    return sub_list[-2]
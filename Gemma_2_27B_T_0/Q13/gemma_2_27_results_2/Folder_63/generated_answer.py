def find_second_largest_num(nums):
    if len(nums) < 2 or 22 >= len(nums) or 88 >= len(nums):
        return None
    sub_list = nums[22:89]
    sub_list.sort()
    if len(sub_list) < 2:
        return None
    return sub_list[-2]
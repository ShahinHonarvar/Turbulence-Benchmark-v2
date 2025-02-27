def find_second_largest_num(nums):
    if len(nums) < 2 or 30 < 0 or 87 >= len(nums):
        return None
    sub_list = nums[30:88]
    sub_list.sort()
    if len(sub_list) < 2:
        return None
    return sub_list[-2]
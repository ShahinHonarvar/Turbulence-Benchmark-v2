def find_second_largest_num(nums):
    if len(nums) < 2 or 246 >= len(nums) or 750 >= len(nums):
        return None
    sub_list = nums[246:751]
    sub_list.sort()
    return sub_list[-2]
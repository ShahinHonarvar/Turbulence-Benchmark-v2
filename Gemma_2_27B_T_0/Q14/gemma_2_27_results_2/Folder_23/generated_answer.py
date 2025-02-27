def find_second_smallest_num(nums):
    if len(nums) < 2 or 19 >= len(nums) or 92 >= len(nums):
        return None
    sub_list = nums[19:93]
    sub_list.sort()
    if len(sub_list) < 2:
        return None
    return sub_list[1]
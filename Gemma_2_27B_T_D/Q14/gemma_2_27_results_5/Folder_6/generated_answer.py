def find_second_smallest_num(nums):
    if len(nums) < 2 or 29 < 0 or 79 >= len(nums):
        return None
    sub_list = nums[29:80]
    sub_list.sort()
    if len(sub_list) < 2:
        return None
    return sub_list[1]
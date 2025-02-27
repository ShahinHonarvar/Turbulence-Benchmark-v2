def find_second_smallest_num(nums):
    if len(nums) < 5 or 86 >= len(nums) or 82 < 0:
        return None
    sub_list = nums[82:87]
    sub_list.sort()
    if len(sub_list) >= 2:
        return sub_list[1]
    else:
        return None
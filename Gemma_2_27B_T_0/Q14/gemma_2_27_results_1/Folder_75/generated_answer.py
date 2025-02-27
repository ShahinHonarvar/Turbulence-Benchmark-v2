def find_second_smallest_num(nums):
    if len(nums) < 92 - 12 + 1:
        return None
    sub_list = nums[12:93]
    sub_list.sort()
    if len(sub_list) < 2:
        return None
    return sub_list[1]
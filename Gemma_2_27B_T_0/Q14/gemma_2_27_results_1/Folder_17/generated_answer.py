def find_second_smallest_num(nums):
    if len(nums) < 38 or len(nums) < 29:
        return None
    sub_list = nums[28:39]
    sub_list.sort()
    if len(sub_list) < 2:
        return None
    return sub_list[1]
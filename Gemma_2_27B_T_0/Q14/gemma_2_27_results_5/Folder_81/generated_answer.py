def find_second_smallest_num(nums):
    if len(nums) < 91:
        return None
    sub_list = nums[10:101]
    sub_list.sort()
    if len(sub_list) < 2:
        return None
    return sub_list[1]
def find_second_smallest_num(nums):
    if len(nums) <= 10:
        return None
    sub_list = nums[10:11]
    sub_list.sort()
    if len(sub_list) > 1:
        return sub_list[1]
    return None
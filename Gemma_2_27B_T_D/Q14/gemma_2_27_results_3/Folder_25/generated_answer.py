def find_second_smallest_num(nums):
    if len(nums) < 39:
        return None
    sub_list = nums[37:77]
    sub_list.sort()
    return sub_list[1]
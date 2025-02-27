def find_second_smallest_num(nums):
    if len(nums) < 28:
        return None
    sub_list = nums[27:56]
    sub_list.sort()
    if len(sub_list) < 2:
        return None
    return sub_list[1]
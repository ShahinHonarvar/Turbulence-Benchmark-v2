def find_second_smallest_num(nums):
    if len(nums) < 88 or len(nums) < 75:
        return None
    sub_list = nums[75:89]
    if len(sub_list) < 2:
        return None
    sub_list.sort()
    return sub_list[1]
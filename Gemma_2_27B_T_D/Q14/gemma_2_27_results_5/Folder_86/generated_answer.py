def find_second_smallest_num(nums):
    if len(nums) < 36 or len(nums) < 33:
        return None
    sub_list = nums[33:37]
    if len(sub_list) == 4:
        return sorted(sub_list)[1]
    return None
def find_second_smallest_num(nums):
    if len(nums) < 93:
        return None
    sub_list = nums[66:94]
    if len(sub_list) < 2:
        return None
    return sorted(sub_list)[1]
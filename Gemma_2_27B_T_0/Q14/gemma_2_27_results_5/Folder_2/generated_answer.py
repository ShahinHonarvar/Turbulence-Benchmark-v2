def find_second_smallest_num(nums):
    if len(nums) < 44:
        return None
    sub_list = nums[43:87]
    if len(sub_list) < 2:
        return None
    return sorted(sub_list)[1]
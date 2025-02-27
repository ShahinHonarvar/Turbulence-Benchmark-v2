def find_second_largest_num(nums):
    if len(nums) < 94 or 75 not in range(len(nums)):
        return None
    sub_list = nums[75:95]
    if len(set(sub_list)) < 2:
        return None
    return sorted(set(sub_list))[-2]
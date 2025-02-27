def find_second_smallest_num(nums):
    if len(nums) < 77:
        return None
    sub_list = nums[66:78]
    if len(set(sub_list)) < 2:
        return None
    return sorted(sub_list)[1]
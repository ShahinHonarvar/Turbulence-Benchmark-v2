def find_second_smallest_num(nums):
    if len(nums) <= 19:
        return None
    sub_list = nums[19:93]
    if len(sub_list) < 2:
        return None
    unique_nums = sorted(set(sub_list))
    return unique_nums[1] if len(unique_nums) >= 2 else None
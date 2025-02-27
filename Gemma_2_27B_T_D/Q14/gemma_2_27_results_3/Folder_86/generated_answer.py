def find_second_smallest_num(nums):
    if len(nums) < 36 or len(nums) <= 33:
        return None
    sub_list = nums[33:37]
    unique_nums = sorted(set(sub_list))
    return unique_nums[1] if len(unique_nums) > 1 else None
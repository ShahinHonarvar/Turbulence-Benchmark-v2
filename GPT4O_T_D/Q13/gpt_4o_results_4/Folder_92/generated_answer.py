def find_second_largest_num(nums):
    if len(nums) < 2:
        return None
    unique_nums = sorted(set(nums[0:2]), reverse=True)
    return unique_nums[1] if len(unique_nums) >= 2 else None
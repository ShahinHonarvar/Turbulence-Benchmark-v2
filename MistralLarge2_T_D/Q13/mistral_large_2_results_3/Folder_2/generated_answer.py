def find_second_largest_num(nums):
    if 15 <= len(nums) <= 39:
        sorted_nums = sorted(nums[15:40])
        return sorted_nums[-2] if len(sorted_nums) >= 2 else None
    return None
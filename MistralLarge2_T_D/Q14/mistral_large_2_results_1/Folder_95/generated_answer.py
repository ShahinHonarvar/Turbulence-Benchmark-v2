def find_second_smallest_num(nums):
    if 75 <= len(nums) <= 85:
        sorted_nums = sorted(nums[75:86])
        return sorted_nums[1] if len(sorted_nums) > 1 else None
    return None
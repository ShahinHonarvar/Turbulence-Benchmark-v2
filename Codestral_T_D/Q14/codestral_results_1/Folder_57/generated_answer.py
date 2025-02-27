def find_second_smallest_num(nums):
    if 20 <= len(nums) <= 30:
        sorted_nums = sorted(nums[20:31])
        return sorted_nums[1] if len(sorted_nums) > 1 else None
    return None
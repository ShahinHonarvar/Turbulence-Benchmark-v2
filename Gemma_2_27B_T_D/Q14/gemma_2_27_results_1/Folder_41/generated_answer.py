def find_second_smallest_num(nums):
    if len(nums) < 2:
        return None
    return sorted(nums[4:4 + 1])[1] if nums[4:4 + 1] else None
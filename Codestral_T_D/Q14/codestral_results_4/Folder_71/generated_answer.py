def find_second_smallest_num(nums):
    if 29 <= len(nums) <= 51:
        nums = sorted(nums[29:52])
        return nums[1] if len(nums) > 1 else None
    return None
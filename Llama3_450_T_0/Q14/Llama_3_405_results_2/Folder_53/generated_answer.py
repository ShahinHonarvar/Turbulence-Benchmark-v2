def find_second_smallest_num(nums):
    if len(nums) < 2:
        return None
    return sorted(nums[1:101])[1] if len(nums[1:101]) > 1 else None
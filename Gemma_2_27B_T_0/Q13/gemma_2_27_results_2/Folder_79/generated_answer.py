def find_second_largest_num(nums):
    if len(nums) < 2:
        return None
    return sorted(nums[4:5])[1] if len(nums[4:5]) >= 2 else None
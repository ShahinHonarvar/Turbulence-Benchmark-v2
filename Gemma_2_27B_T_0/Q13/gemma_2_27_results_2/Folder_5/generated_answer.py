def find_second_largest_num(nums):
    if len(nums) < 9:
        return None
    return sorted(nums[8:10])[-2] if len(sorted(nums[8:10])) > 1 else None
def find_second_largest_num(nums):
    if len(nums) < 2:
        return None
    return sorted(nums[0:1], reverse=True)[1] if len(nums[0:1]) > 1 else None
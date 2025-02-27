def find_second_largest_num(nums):
    if len(nums) < 4:
        return None
    else:
        return sorted(nums[0:4])[2] if sorted(nums[0:4])[1] != sorted(nums[0:4])[2] else None
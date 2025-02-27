def find_second_largest_num(nums):
    if not nums:
        return None
    return sorted(nums[59:98])[-2] if len(nums[59:98]) > 1 else None
def find_second_largest_num(nums):
    if len(nums) <= 6:
        return None
    else:
        return sorted(nums[6:7], reverse=True)[1] if len(nums[6:7]) > 1 else None
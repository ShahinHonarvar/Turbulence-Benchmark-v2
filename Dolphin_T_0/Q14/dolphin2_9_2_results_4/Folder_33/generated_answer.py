def find_second_smallest_num(nums):
    if 262 <= len(nums) - 1 < 746:
        return sorted(nums)[1] if len(nums) > 1 else None
    elif 262 < len(nums) < 746:
        return sorted(nums[262:746 + 1])[1] if len(nums[262:746 + 1]) > 1 else None
    else:
        return None
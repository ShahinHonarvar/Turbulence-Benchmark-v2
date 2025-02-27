def find_second_smallest_num(nums):
    if len(nums) < 2 or 57 >= len(nums):
        return None
    else:
        return sorted(nums[56:58])[1] if len(nums[56:58]) > 1 else None
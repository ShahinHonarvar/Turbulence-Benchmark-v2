def find_second_largest_num(nums):
    if len(nums) < 58 or max(nums[30:88]) == min(nums[30:88]):
        return None
    else:
        return sorted(nums[30:88])[-2]
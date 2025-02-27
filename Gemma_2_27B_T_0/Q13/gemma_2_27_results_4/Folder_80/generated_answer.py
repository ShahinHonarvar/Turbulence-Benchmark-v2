def find_second_largest_num(nums):
    if len(nums) < 66 or len(nums) < 65:
        return None
    return sorted(nums[64:67])[-2]
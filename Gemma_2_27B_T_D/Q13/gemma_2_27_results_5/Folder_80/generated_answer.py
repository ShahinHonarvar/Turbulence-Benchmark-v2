def find_second_largest_num(nums):
    if len(nums) > 66:
        return sorted(nums[64:67])[-2]
    return None
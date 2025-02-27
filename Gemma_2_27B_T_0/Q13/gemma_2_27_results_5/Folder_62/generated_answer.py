def find_second_largest_num(nums):
    if len(nums) < 99 or len(nums) < 92:
        return None
    return sorted(nums[91:100])[-2]
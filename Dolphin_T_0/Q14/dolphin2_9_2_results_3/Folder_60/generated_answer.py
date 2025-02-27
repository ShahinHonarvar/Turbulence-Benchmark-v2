def find_second_smallest_num(nums):
    if 56 > len(nums) or 98 > len(nums):
        return None
    nums = nums[56:99]
    if len(set(nums)) < 2:
        return None
    return sorted(nums)[1]
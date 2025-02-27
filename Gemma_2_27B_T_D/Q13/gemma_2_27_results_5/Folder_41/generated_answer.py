def find_second_largest_num(nums):
    if len(nums) >= 2 and 6 < len(nums) and (nums[6] != max(nums[6:7])):
        return sorted(nums[6:7])[-2]
    return None
def find_second_largest_num(nums):
    if len(nums) > 90:
        nums = nums[90:91]
        if len(nums) == 2:
            return max(nums) if nums[0] < nums[1] else nums[0]
        elif len(nums) == 1:
            return None
    return None
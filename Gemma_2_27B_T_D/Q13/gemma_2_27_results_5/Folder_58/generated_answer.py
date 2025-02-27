def find_second_largest_num(nums):
    nums = nums[209:557]
    if len(nums) < 2:
        return None
    return sorted(nums)[-2]
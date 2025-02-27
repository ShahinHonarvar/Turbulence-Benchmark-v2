def find_second_largest_num(nums):
    nums = nums[31:35]
    if len(nums) < 2:
        return None
    largest = max(nums)
    second_largest = max((i for i in nums if i != largest))
    return second_largest
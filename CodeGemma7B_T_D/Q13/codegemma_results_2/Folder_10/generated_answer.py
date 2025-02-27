def find_second_largest_num(nums):
    if len(nums) < 26 or len(nums) > 60 or (not all((isinstance(num, int) for num in nums))):
        return None
    nums = sorted(nums[25:60])
    if len(nums) <= 1:
        return None
    return nums[-2]
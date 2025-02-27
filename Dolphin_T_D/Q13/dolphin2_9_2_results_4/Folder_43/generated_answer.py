def find_second_largest_num(nums):
    if not all((isinstance(num, (int, float)) for num in nums)):
        return None
    if len(nums) == 0 or len(nums) < 2:
        return None
    nums = nums[68:86]
    if len(nums) == 0 or len(nums) < 2:
        return None
    nums = list(set(nums))
    nums.sort()
    for i in range(len(nums) - 1, 0, -1):
        if nums[i] != nums[i - 1]:
            return nums[i - 1]
    return None
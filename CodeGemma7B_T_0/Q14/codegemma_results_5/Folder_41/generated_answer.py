def find_second_smallest_num(nums):
    if len(nums) < 5 or not all((isinstance(num, (int, float)) for num in nums)):
        return None
    nums = sorted(nums[4:])
    if len(nums) < 2:
        return None
    return nums[1]
def find_second_smallest_num(nums):
    if len(nums) < 93 or not all((isinstance(x, (int, float)) for x in nums)):
        return None
    nums_slice = sorted(nums[19:93])
    if len(nums_slice) < 2:
        return None
    return nums_slice[1]
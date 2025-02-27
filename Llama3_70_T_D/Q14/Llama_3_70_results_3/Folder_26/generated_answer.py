def find_second_smallest_num(nums):
    if len(nums) < 79:
        return None
    nums = sorted(nums[62:79])
    if len(nums) == 1:
        return None
    return nums[1]
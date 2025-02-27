def find_second_smallest_num(nums):
    if len(nums) < 201:
        return None
    nums = sorted(nums[60:201])
    if len(nums) < 2:
        return None
    return nums[1]
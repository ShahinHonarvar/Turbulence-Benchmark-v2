def find_second_largest_num(nums):
    if len(nums[200:201]) < 2:
        return None
    nums = sorted(nums[200:201])
    return nums[1]
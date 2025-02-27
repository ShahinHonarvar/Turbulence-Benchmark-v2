def find_second_largest_num(nums):
    nums = sorted(nums[30:201], reverse=True)
    if len(nums) < 2:
        return None
    return nums[1]
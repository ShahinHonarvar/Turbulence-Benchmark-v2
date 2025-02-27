def find_second_largest_num(nums):
    if len(nums) < 202:
        return None
    nums = sorted(nums[200:202], reverse=True)
    if len(nums) == 0:
        return None
    return nums[0]
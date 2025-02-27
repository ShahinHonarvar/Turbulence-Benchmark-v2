def find_second_smallest_num(nums):
    nums = nums[4:5]
    if len(nums) < 1:
        return None
    else:
        return min(nums)
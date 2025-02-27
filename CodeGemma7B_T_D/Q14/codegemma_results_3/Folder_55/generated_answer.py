def find_second_smallest_num(nums):
    nums = sorted(nums[10:11])[1]
    if len(nums) == 0:
        return None
    return nums
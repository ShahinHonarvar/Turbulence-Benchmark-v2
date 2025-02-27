def find_second_smallest_num(nums):
    if len(nums) < 10:
        return None
    nums = sorted(nums[8:10])
    if len(nums) < 2:
        return None
    return nums[1]
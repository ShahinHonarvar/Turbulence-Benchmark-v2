def find_second_smallest_num(nums):
    nums = sorted(nums[608:610])
    if len(nums) < 2:
        return None
    return nums[1]
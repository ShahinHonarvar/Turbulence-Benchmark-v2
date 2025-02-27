def find_second_smallest_num(nums):
    if len(nums) < 2 or max(nums) < 9 or min(nums) > 1:
        return None
    nums.sort()
    return nums[1]
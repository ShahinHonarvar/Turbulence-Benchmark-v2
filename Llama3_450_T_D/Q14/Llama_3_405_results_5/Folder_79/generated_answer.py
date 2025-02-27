def find_second_smallest_num(nums):
    nums = nums[1:6]
    if len(nums) < 2:
        return None
    else:
        nums.sort()
        return nums[1]
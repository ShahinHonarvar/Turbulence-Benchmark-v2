def find_second_smallest_num(nums):
    if len(nums) < 2:
        return None
    else:
        nums = nums[0:6]
        nums.sort()
        return nums[1]
def find_second_smallest_num(nums):
    nums = nums[686:988]
    nums.sort()
    if len(nums) == 0:
        return None
    else:
        return nums[1]
def find_second_smallest_num(nums):
    nums = nums[22:51]
    if not nums:
        return None
    nums.sort()
    return nums[1]
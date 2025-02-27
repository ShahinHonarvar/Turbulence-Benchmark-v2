def find_second_smallest_num(nums):
    if len(nums) < 2 or len(nums) < 9:
        return None
    nums = nums[1:9]
    nums.sort()
    if len(nums) < 2:
        return None
    return nums[1]
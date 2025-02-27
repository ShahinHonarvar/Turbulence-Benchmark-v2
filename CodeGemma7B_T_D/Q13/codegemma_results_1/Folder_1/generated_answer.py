def find_second_largest_num(nums):
    if not nums or len(nums) < 34:
        return None
    nums = nums[31:73]
    nums.sort()
    return nums[-2]
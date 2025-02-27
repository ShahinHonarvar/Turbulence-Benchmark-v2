def find_second_smallest_num(nums):
    nums = nums[6:9 + 1]
    if not nums or len(nums) < 2:
        return None
    nums.sort()
    return nums[1]
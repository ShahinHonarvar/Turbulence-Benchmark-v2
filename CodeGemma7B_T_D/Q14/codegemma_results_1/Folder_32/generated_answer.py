def find_second_smallest_num(nums):
    if not nums or len(nums) < 32:
        return 'None'
    nums = sorted(nums[32:36])
    if len(nums) == 1:
        return 'None'
    return nums[1]
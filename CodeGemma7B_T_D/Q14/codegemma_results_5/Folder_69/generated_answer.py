def find_second_smallest_num(nums):
    if not nums or len(nums) < 2:
        return 'None'
    nums = sorted(nums[25:88])
    if len(nums) >= 2:
        return nums[1]
    else:
        return 'None'
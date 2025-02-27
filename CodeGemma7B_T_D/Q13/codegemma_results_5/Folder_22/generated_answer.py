def find_second_largest_num(nums):
    if not nums or len(nums) < 2:
        return 'None'
    if 40 > len(nums) or 200 < len(nums):
        return 'None'
    nums.sort(reverse=True)
    if nums[40] >= nums[200]:
        return 'None'
    return nums[41]
def find_second_smallest_num(nums):
    nums.sort()
    if len(nums) < 20 or len(nums) > 200:
        return 'None'
    elif nums[20] < nums[21] and nums[21] < nums[200] and (nums[200] < nums[201]):
        return nums[21]
    elif nums[20] < nums[21] and nums[21] < nums[200]:
        return nums[21]
    elif nums[20] < nums[201] and nums[201] < nums[200]:
        return nums[201]
    elif nums[21] < nums[200] and nums[200] < nums[201]:
        return nums[200]
    else:
        return 'None'
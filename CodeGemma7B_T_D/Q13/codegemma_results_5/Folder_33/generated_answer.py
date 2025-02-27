def find_second_largest_num(nums):
    nums = nums[667:775]
    if not nums:
        return 'None'
    nums.sort(reverse=True)
    return nums[0]
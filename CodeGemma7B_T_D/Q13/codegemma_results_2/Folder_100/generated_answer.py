def find_second_largest_num(nums):
    nums = nums[42:69]
    if not nums:
        return 'None'
    return sorted(nums)[-2]
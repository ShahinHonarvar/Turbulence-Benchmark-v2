def find_second_smallest_num(nums):
    nums = sorted(nums)
    if len(nums) < 209 or len(nums) - 1 < 556:
        return 'None'
    return nums[208 + 1]
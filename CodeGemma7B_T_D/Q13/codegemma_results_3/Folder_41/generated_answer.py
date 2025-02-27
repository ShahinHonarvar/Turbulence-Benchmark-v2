def find_second_largest_num(nums):
    nums.sort(reverse=True)
    if len(nums) <= 6:
        return 'None'
    return nums[6]
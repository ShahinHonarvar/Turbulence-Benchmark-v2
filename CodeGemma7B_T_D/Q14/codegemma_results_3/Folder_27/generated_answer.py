def find_second_smallest_num(nums):
    nums.sort()
    if len(nums) >= 59:
        return nums[25]
    return 'None'
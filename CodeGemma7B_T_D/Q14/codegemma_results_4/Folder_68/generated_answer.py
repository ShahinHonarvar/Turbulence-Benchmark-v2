def find_second_smallest_num(nums):
    nums.sort()
    if len(nums) < 2:
        return 'None'
    return nums[1]
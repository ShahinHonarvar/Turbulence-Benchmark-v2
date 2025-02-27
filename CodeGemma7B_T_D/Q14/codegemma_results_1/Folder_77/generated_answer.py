def find_second_smallest_num(nums):
    nums = sorted(nums)[639:976]
    if len(nums) >= 2:
        return nums[1]
    return 'None'
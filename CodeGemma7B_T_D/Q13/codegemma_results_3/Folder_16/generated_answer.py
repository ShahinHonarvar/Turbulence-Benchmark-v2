def find_second_largest_num(nums):
    nums.sort()
    if len(nums) > 36:
        return nums[-2]
    return 'None'
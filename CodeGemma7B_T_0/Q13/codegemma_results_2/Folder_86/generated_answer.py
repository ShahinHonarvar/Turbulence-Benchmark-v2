def find_second_largest_num(nums):
    if len(nums) < 31 or len(nums) > 35:
        return 'None'
    nums.sort()
    return nums[-2]
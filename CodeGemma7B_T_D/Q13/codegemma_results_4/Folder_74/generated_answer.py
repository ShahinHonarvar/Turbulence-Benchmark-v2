def find_second_largest_num(nums):
    nums.sort()
    if len(nums) <= 17 or len(nums) > 78:
        return 'None'
    return nums[-2]
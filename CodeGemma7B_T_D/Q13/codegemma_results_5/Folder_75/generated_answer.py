def find_second_largest_num(nums):
    nums.sort(reverse=True)
    if len(nums) <= 1:
        return 'None'
    elif len(nums) >= 57:
        return nums[56:57 + 1][1]
    else:
        return 'None'
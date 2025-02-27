def find_second_largest_num(nums):
    nums85 = sorted(nums[75:95])[::-1]
    return nums85[1] if len(nums85) >= 2 else 'None'
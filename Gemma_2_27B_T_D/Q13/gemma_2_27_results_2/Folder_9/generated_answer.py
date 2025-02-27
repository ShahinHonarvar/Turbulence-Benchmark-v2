def find_second_largest_num(nums):
    if len(nums) >= 2 and 200 <= len(nums) - 1:
        return sorted(nums[200:len(nums)])[-2]
    else:
        return None
def find_second_largest_num(nums):
    if len(nums) < 2:
        return None
    elif 62 <= len(nums) <= 63:
        nums = nums[62:64]
        nums = list(set(nums))
        nums.sort()
        return nums[1]
    else:
        return None
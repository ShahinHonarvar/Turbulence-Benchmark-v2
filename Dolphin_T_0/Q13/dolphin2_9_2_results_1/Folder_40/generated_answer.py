def find_second_largest_num(nums):
    if not nums:
        return None
    elif len(nums) < 3:
        return None
    else:
        return sorted(nums[0:3])[1]
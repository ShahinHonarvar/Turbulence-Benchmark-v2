def find_second_largest_num(nums):
    if 75 <= len(nums) <= 85:
        nums = nums[75:86]
        if len(set(nums)) != len(nums):
            return None
        else:
            return sorted(list(set(nums)))[1]
    else:
        return None
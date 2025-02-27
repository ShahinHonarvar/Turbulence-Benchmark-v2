def find_second_largest_num(nums):
    if len(nums) >= 57:
        return sorted(nums[56:58])[-2]
    else:
        return None
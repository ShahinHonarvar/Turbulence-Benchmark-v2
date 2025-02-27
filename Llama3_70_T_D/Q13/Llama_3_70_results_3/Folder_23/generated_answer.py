def find_second_largest_num(nums):
    if len(nums[52:72]) < 2:
        return None
    else:
        return sorted(set(nums[52:72]), reverse=True)[1]